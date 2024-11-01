from fastapi import FastAPI

app = FastAPI(title="Simple HTTP")

@app.get("/")
async def root():
    return {"message": "Hello World"}
