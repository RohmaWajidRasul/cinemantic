# Implemented by Bimnet, Filipe and Rohma
from fastapi import FastAPI, Form, UploadFile, File, HTTPException, BackgroundTasks
from fastapi.responses import JSONResponse
from settings import POSTGRES, API_SERVICE_URL, MODEL_UPDATE_SECRET
from movie_recommender import MovieRecommender
import asyncio
import pandas as pd
from pydantic import BaseModel
from dataHandler import validateCSV, addMovies, getRecommended, updateEmb, addGenres, updateRecsTable, getVersion
import requests
from database import engine
from settings import POSTGRES


class FineTuneParameter(BaseModel):
    version: str
    batch_size: int
    epochs: int

def run_fine_tuning(df, params):

    v = params.get("version")
    api_url = f"{API_SERVICE_URL}/api/v1/admin/model-versions/{v}/"

    try:
        recommender = MovieRecommender(
            df=df,
            batch_size=params.get("batch_size", 128),
            epochs=params.get("epochs", 2)
        )

        recommender.setup_recommender(True)

        addMovies(df)
        addGenres(df)
        updateEmb(recommender)
        updateRecsTable()

        payload = {"status": "ready"}

    except Exception as e:
        print("Fine-tuning failed:", e)
        payload = {"status": "failed"}

    requests.patch(
        api_url,
        json=payload,
        headers={"X-MODEL-SECRET": MODEL_UPDATE_SECRET},
    )


app = FastAPI()

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/api/v1/admin/fine-tune/")
def train(background_tasks: BackgroundTasks, version: str = Form(...), batch_size: int = Form(...), 
          epochs: int = Form(...), file: UploadFile = File(...)):

    print("POST RECEIVED")
    params_dict = {
        "version": version,
        "batch_size": batch_size,
        "epochs": epochs
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

