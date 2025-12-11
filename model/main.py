from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from .settings import POSTGRES

app = FastAPI()

@app.get("/health")
def health():
    return {"db": POSTGRES}

@app.post("/api/v1/movies/fine-tune/")
async def train(file: UploadFile = File(...)):

    if not file:
        raise HTTPException(
            status_code=400,
            detail="CSV file is required."
        )

    try:
        file_bytes = await file.read()
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to read uploaded file: {e}"
        )

    try:
        ## call model 
        return JSONResponse(
            status_code=200,
            content={"detail": "Training completed successfully."}
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
        results = 
        return JSONResponse(
            status_code=200,
            content={"detail": "Training completed successfully.", **results}
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Recommendation service failed: {e}"
        )

