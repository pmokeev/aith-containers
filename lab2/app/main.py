from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine, text
import os

app = FastAPI(title="Hello World DB")

DATABASE_URL = f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@{os.getenv('POSTGRES_HOST')}:{os.getenv('POSTGRES_PORT')}/{os.getenv('POSTGRES_DB')}"
engine = create_engine(DATABASE_URL)

@app.get("/")
async def root():
    try:
        with engine.connect() as connection:
            result = connection.execute(text("SELECT message FROM hello_messages ORDER BY id DESC LIMIT 1"))
            message = result.fetchone()[0]
        return {"message": message}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health():
    return {"status": "healthy"}