from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI(title="DevOps Pipeline Demo")

@app.get("/health")
def health_check():
    return JSONResponse(content={"status": "ok"})

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI DevOps Project!"}
