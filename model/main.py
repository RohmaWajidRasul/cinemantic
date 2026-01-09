from fastapi import FastAPI, Form, UploadFile, File, HTTPException, BackgroundTasks
from fastapi.responses import JSONResponse
from settings import API_SERVICE_URL, MODEL_UPDATE_SECRET
from movie_recommender import MovieRecommender
import pandas as pd
from dataHandler import validateCSV, addMovies, getRecommended, updateEmb, addGenres, updateRecsTable
import requests
from database import engine

def run_fine_tuning(df, params):

    v = params.get("new_version")
    api_url = f"{API_SERVICE_URL}/api/v1/internal/model-versions/{v}/"

    use_default = False

    try:
        recommender = MovieRecommender(
            df=df,
            batch_size=params.get("batch_size", 128),
            epochs=params.get("epochs", 2)
        )

        if params.get("base_model") == "default":
            use_default = True

        precision_before, precision_after = recommender.setup_recommender(use_default)

        THRESHOLD = 0.05

        drop_ratio = (precision_before - precision_after) / precision_before
        bad_model = drop_ratio > THRESHOLD

        addMovies(df)
        addGenres(df)

        if bad_model:
            print("Bad fine-tuned model detected. Using previous model...")
            recommender._reset_old_model()

            new_ids = df["id"].tolist()
            updateEmb(recommender, only_new=True, new_ids=new_ids)

            updateRecsTable()

            payload = {
                "status": "ready",
                "precision_before": precision_before,
                "precision_after": precision_after,
                "detail": "Model not deployed due to precision drop > 5%"
            }
        else:
            updateEmb(recommender)

            updateRecsTable()

            payload = {
                "status": "current",
                "precision_before": precision_before,
                "precision_after": precision_after,
                "detail": "Model was deployed"
            }

    except Exception as e:
        print("Fine-tuning failed:", e)
        payload = {
            "status": "failed",
            "detail": f"Fine-tuning failed: {e}" 
        }

    requests.patch(
        api_url,
        json=payload,
        headers={"X-MODEL-SECRET": MODEL_UPDATE_SECRET},
    )

def run_rollback(version: str):
    api_url = f"{API_SERVICE_URL}/api/v1/internal/model-versions/{version}/"

    try:
        print(f"ROLLBACK STARTED for version {version}")

        recommender = MovieRecommender()
        updateEmb(recommender)
        updateRecsTable()

        payload = {
            "status": "current",
            "detail": "Rollback succeeded"
        }
    except Exception as e:
        print("Rollback failed:", e)
        payload = {
            "status": "failed",
            "detail": f"Rollback failed: {e}" 
        }

    requests.patch(
        api_url,
        json=payload,
        headers={"X-MODEL-SECRET": MODEL_UPDATE_SECRET},
    )


app = FastAPI()

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/api/v1/fine-tune/")
def train(background_tasks: BackgroundTasks, base_model: str = Form(...), batch_size: int = Form(...), 
          epochs: int = Form(...), new_version: str = Form(...), file: UploadFile = File(...)):

    print("FINE-TUNE RECEIVED")
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
        df = pd.read_csv(file.file)
        df = validateCSV(df)

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to read uploaded file: {e}"
        )

    try:
        ## Fine-tuning + inserting into db
        print("FINE TUNING STARTS")
        background_tasks.add_task(run_fine_tuning, df, params_dict)

        return JSONResponse(
            status_code=200,
            content={"detail": "Training started."}
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Training failed due to an internal error: {e}"
        )

@app.post("/api/v1/model-versions/{version}/rollback/")
def rollback_model(version: str, background_tasks: BackgroundTasks):

    try: 
        print(f"ROLLING BACK MODEL {version}")
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
    print(payload)
    title = payload.get("title", "")
    genres = payload.get("genres", "")
    overview = payload.get("overview", "")

    if not title or not genres or not overview:
        raise HTTPException(
            status_code=400,
            detail="Missing important data."
        )

    try:
        recommender = MovieRecommender()
        ids = []
        emb = recommender.encodeNewMovie(ids, title, genres)

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
        raise HTTPException(
            status_code=500,
            detail=f"Recommendation service failed: {e}"
        )

