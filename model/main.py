from fastapi import FastAPI, Form, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from settings import POSTGRES, API_SERVICE_URL, MODEL_UPDATE_SECRET
from movie_recommender import MovieRecommender
import asyncio
import pandas as pd
from pydantic import BaseModel
from dataHandler import validateCSV, addMovies, getRecommended, updateEmb, addGenres, updateRecsTable, getVersion
import requests
from sqlalchemy import create_engine
from settings import POSTGRES

DATABASE_URL = (
    f"postgresql://{POSTGRES['USER']}:{POSTGRES['PASSWORD']}"
    f"@{POSTGRES['HOST']}:{POSTGRES['PORT']}/{POSTGRES['NAME']}"
)

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

    api_url = f"{API_SERVICE_URL}/api/v1/admin/model-versions/{v}/"
    print(api_url)
    payload = {"status": "ready"}
    requests.patch(api_url, json=payload, headers={"X-MODEL-SECRET": MODEL_UPDATE_SECRET},)

app = FastAPI()

@app.get("/health")
def health():
    return {"db": POSTGRES}

@app.post("/api/v1/admin/fine-tune/")
async def train(model_name: str = Form(...), batch_size: int = Form(...), epochs: int = Form(...), file: UploadFile = File(...)):

    params_dict = {
        "model_name": model_name,
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

        engine = create_engine(DATABASE_URL, echo=False, future=True)
        with engine.begin() as conn:

            results = getRecommended(emb, conn)

        return JSONResponse(
            status_code=200,
            content={
            "detail": "Recommendations fetched successfully.",
            "results": results
        }
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Recommendation service failed: {e}"
        )

