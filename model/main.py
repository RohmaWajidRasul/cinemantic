# Implemented by Bimnet, Filipe and Rohma
from fastapi import FastAPI, Form, UploadFile, File, HTTPException, BackgroundTasks
from fastapi.responses import JSONResponse
from settings import API_SERVICE_URL, MODEL_UPDATE_SECRET, MODEL_BUCKET_NAME
from movie_recommender import MovieRecommender
import pandas as pd
from dataHandler import validateCSV, addMovies, getRecommended, updateEmb, addGenres, updateRecsTable
import requests
from database import engine
import os
from google.cloud import storage
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
recommender: MovieRecommender | None = None

def download_model_from_gcs(bucket_name, src_folder="current_model/", dst_folder="./models/current"):
    """Downloads the model directory from GCS on startup."""
    try:
        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)
        blobs = bucket.list_blobs(prefix="current_model/")
        
        found = False
        for blob in blobs:
            found = True
            # Remove prefix to get relative path
            rel_path = blob.name.replace(src_folder, "")
            if not rel_path: continue
            
            local_path = os.path.join(dst_folder, rel_path)
            os.rmdir(local_path)
            os.makedirs(os.path.dirname(local_path))
            blob.download_to_filename(local_path)
        
        if found:
            logging.info("Model downloaded from GCS.")
        else:
            logging.info("No model found in GCS, using default/init.")
    except Exception as e:
        logging.error(f"Failed to download model from GCS: {e}", exc_info=True)
    
def upload_model_to_gcs(bucket_name, src_folder, dst_folder="current_model/"):
    """Uploads the fine-tuned model to GCS."""
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    
    try:
        logging.info(f"Starting upload of model from {src_folder} to GCS bucket: {bucket_name}")
        for root, dirs, files in os.walk(src_folder):
            for file in files:
                local_path = os.path.join(root, file)
                rel_path = os.path.relpath(local_path, src_folder)
                blob_path = f"{dst_folder}{rel_path}"
                
                blob = bucket.blob(blob_path)
                logging.info(f"Uploading {local_path} to {blob_path}")
                blob.upload_from_filename(local_path)
        logging.info("Model uploaded to GCS successfully.")
    except Exception as e:
        logging.error(f"Failed to upload model from GCS: {e}", exc_info=True)

def run_fine_tuning(df, params):

    new_version = params.get("new_version")
    base_version = params.get("base_model")
    api_url = f"{API_SERVICE_URL}/api/v1/internal/model-versions/{new_version}/"

    use_default = False

    try:
        logging.info(f"Starting fine-tuning for model version {new_version} with params: {params}")
        logging.info(f"API URL for status updates: {api_url}")

        if params.get("base_model") == "default":
            use_default = True
        
        else:
            download_model_from_gcs(MODEL_BUCKET_NAME, src_folder=f"all_models/{base_version}/", dst_folder="./models/base_model")

        precision_before, precision_after = recommender.setup_recommender(use_default, new_version, df=df,
            batch_size=params.get("batch_size", 128),
            epochs=params.get("epochs", 2))

        THRESHOLD = 0.05

        drop_ratio = (precision_before - precision_after) / precision_before
        bad_model = drop_ratio > THRESHOLD

        addMovies(df)
        addGenres(df)

        new_model_path = recommender.new_model_path_prefix + f"/{new_version}"
        upload_model_to_gcs(MODEL_BUCKET_NAME, new_model_path, dst_folder=f"all_models/{new_version}/")

        if bad_model:
            logging.info("Bad fine-tuned model detected. Using previous model...")

            new_ids = df["id"].tolist()
            updateEmb(recommender, only_new=True, new_ids=new_ids)

            # TODO: Upload model to bucket
            logging.info("Previous model re-uploaded to GCS successfully.")

            updateRecsTable()

            payload = {
                "status": "ready",
                "precision_before": precision_before,
                "precision_after": precision_after,
                "detail": "Model not deployed due to precision drop > 5%"
            }
        else:
            # Only upload the new weights to GCS if the model is good
            logging.info("Fine-tuned model is good. Uploading to GCS.")
            recommender._set_new_model(new_version)

            updateEmb(recommender)

            updateRecsTable()

            upload_model_to_gcs(MODEL_BUCKET_NAME, new_model_path)

            payload = {
                "status": "current",
                "precision_before": precision_before,
                "precision_after": precision_after,
                "detail": "Model was deployed"
            }

    except Exception as e:
        logging.error(f"Fine-tuning failed: {e}", exc_info=True)
        payload = {
            "status": "failed",
            "detail": f"Fine-tuning failed: {e}" 
        }

    try:
        requests.patch(
            api_url,
            json=payload,
            headers={"X-MODEL-SECRET": MODEL_UPDATE_SECRET},
        )
        logging.info(f"Patched model version status to '{payload.get('status')}' for version {new_version}. Detail: {payload.get('detail')}")
    except requests.exceptions.RequestException as req_e:
        logging.error(f"Failed to patch model version status to Django API at {api_url}: {req_e}", exc_info=True)

def run_rollback(version: str):
    api_url = f"{API_SERVICE_URL}/api/v1/internal/model-versions/{version}/"

    try:
        print(f"ROLLBACK STARTED for version {version}")

        recommender._reset_model()

        updateEmb(recommender)
        updateRecsTable()

        upload_model_to_gcs(MODEL_BUCKET_NAME, "./models/current/")

        payload = {
            "status": "current",
            "detail": "Rollback succeeded"
        }
    except Exception as e:
        logging.error(f"Rollback failed: {e}", exc_info=True)
        payload = {
            "status": "failed",
            "detail": f"Rollback failed: {e}" 
        }

    try:
        requests.patch(
            api_url,
            json=payload,
            headers={"X-MODEL-SECRET": MODEL_UPDATE_SECRET},
        )
        logging.info(f"Patched model version status to '{payload.get('status')}' for version {version}. Detail: {payload.get('detail')}")
    except requests.exceptions.RequestException as req_e:
        logging.error(f"Failed to patch model version status to Django API at {api_url} during rollback: {req_e}", exc_info=True)


app = FastAPI()

@app.on_event("startup")
def startup():
    download_model_from_gcs(MODEL_BUCKET_NAME)
    global recommender
    recommender = MovieRecommender()
    logging.info("MovieRecommender loaded")

@app.get("/health")
def health():
    return {"status": "healthy" if recommender and recommender.model else "unready"}

@app.post("/api/v1/fine-tune/")
def train(background_tasks: BackgroundTasks, base_model: str = Form(...), batch_size: int = Form(...), 
          epochs: int = Form(...), new_version: str = Form(...), file: UploadFile = File(...)):

    logging.info(f"Fine-tune request received for new_version='{new_version}', base_model='{base_model}'.")
    params_dict = {
        "base_model": base_model,
        "batch_size": batch_size,
        "epochs": epochs,
        "new_version": new_version
    }

    if not file:
        raise HTTPException(
            status_code=400,
            detail="CSV file is required."
        )

    try:
        # Validation
        logging.info("Reading and validating uploaded CSV file.")
        df = pd.read_csv(file.file)
        df = validateCSV(df)
        logging.info("CSV file validated successfully.")
    except Exception as e:
        logging.error(f"Failed to read or validate uploaded file: {e}", exc_info=True)
        raise HTTPException(
            status_code=500,
            detail=f"Failed to read uploaded file: {e}"
        )

    try:
        ## Fine-tuning + inserting into db
        logging.info("Initiating background fine-tuning task.")
        background_tasks.add_task(run_fine_tuning, df, params_dict)

        return JSONResponse(
            status_code=202,
            content={"detail": "Training started."}
        )
    except Exception as e:
        logging.error(f"Failed to start background fine-tuning task: {e}", exc_info=True)
        raise HTTPException(
            status_code=500,
            detail=f"Training failed due to an internal error: {e}"
        )

@app.post("/api/v1/model-versions/{version}/rollback/")
def rollback_model(version: str, background_tasks: BackgroundTasks):

    try:
        download_model_from_gcs(MODEL_BUCKET_NAME, src_folder=f"all_models/{version}/", dst_folder="./models/current")
        logging.info(f"ROLLING BACK MODEL {version}")
        background_tasks.add_task(run_rollback, version)

        return JSONResponse(
            status_code=200,
            content={"detail": f"Rollback initialized for model {version}"}
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Rollback failed due to an internal error: {e}"
        )  

@app.get("/api/v1/movies/")
async def recommend(payload: dict):
    logging.info(f"Received recommendation request with payload: {payload}")
    title = payload.get("title", "")
    genres = payload.get("genres", "")
    overview = payload.get("overview", "")

    if not title or not genres or not overview:
        raise HTTPException(
            status_code=400,
            detail="Missing important data."
        )

    try:
        logging.info(f"Generating recommendations for title: '{title}', genres: '{genres}'")
        recommender = MovieRecommender()
        ids = []
        emb = recommender.encodeNewMovie(ids, title, genres)

        logging.info("Fetching recommendations from database.")
        with engine.begin() as conn:
            results = getRecommended(emb, conn)

        return JSONResponse(
            status_code=200,
            content={
            "detail": "Recommendations fetched successfully.",
            "recommendations": results
        }
        )
    except Exception as e:
        logging.error(f"Recommendation service failed: {e}", exc_info=True)
        raise HTTPException(
            status_code=500,
            detail=f"Recommendation service failed: {e}"
        )
