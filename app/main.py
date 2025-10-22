from fastapi import FastAPI

app = FastAPI(title="fast-crud")

@app.get("/")
def read_root():
    return {"message": "fast-crud API is running"}


@app.get("/health")
def health():
    return {"stuts": "ok"}
