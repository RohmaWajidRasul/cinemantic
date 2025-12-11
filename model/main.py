from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from .settings import POSTGRES
from movie_recommender import MovieRecommender
import asyncio
import pandas as pd
from pydantic import BaseModel
from dataHandler import validateCSV, insertCSV

class FineTuneParameter(BaseModel):
    model_name: str
    batch_size: int
    epochs: int

async def run_fine_tuning(df, params):
    recommender = MovieRecommender(
        df=df,
        model_name=params["model_name"],
        batch_size=params["batch_size"],
        epochs=params["epochs"]
    )
    recommender.setup_recommender(True)

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
        ### TODO:
        insertCSV(df)

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to read uploaded file: {e}"
        )

    try:
        ## Fine-tuning
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

@app.post("/api/v1/movies/")
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
        #results = 
        return JSONResponse(
            status_code=200,
            content={"detail": "Training completed successfully.", **results}
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Recommendation service failed: {e}"
        )

