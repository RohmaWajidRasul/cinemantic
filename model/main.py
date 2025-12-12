from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from .settings import POSTGRES, AI_SERVICE_URL
from movie_recommender import MovieRecommender, encodeNewMovie
import asyncio
import pandas as pd
from pydantic import BaseModel
from dataHandler import validateCSV, addMovies, getRecommended, updateEmb, addGenres, updateRecsTable, getVersion
import requests

class FineTuneParameter(BaseModel):
    model_name: str
    batch_size: int
    epochs: int

async def run_fine_tuning(df, params):
    recommender = MovieRecommender(
        df=df,
        batch_size=params.get("batch_size", 128),
        epochs=params.get("epochs", 2)  
    )
    recommender.setup_recommender(True)

    ### TODO:
    addMovies(df)
    addGenres(df)
    updateEmb(recommender)
    updateRecsTable()

    v = getVersion()

    ai_url = AI_SERVICE_URL + "/api/v1/admin/model-versions/{v}", 
    payload = {"status": "ready"}
    backend_resp = requests.post(ai_url, payload)

app = FastAPI()

@app.get("/health")
def health():
    return {"db": POSTGRES}

@app.post("/api/v1/movies/fine-tune/")
async def train(params: FineTuneParameter, file: UploadFile = File(...)):
    
    params_dict = params.model_dump()

    if not file:
        raise HTTPException(
            status_code=400,
            detail="CSV file is required."
        )

    try:
        # Validation
        file_bytes = await file.read()
        df = pd.read_csv(file_bytes)
        df = validateCSV(df)

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to read uploaded file: {e}"
        )

    try:
        ## Fine-tuning + inserting into db
        asyncio.create_task(run_fine_tuning(df, params_dict))

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
        results = getRecommended(emb)
        return JSONResponse(
            status_code=200,
            content={"detail": "Training completed successfully.", **results}
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Recommendation service failed: {e}"
        )

