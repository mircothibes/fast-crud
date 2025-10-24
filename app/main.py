from fastapi import FastAPI
from app.database import Base, engine
from app.routers.users import router as users_router


app = FastAPI(title="fast-crud")

# Temporary: create tables at startup
Base.metadata.create_all(bind=engine

@app.get("/")
def read_root():
    return {"message": "fast-crud API is running"}


@app.get("/health")
def health():
    return {"stuts": "ok"}


# Routers
app.include_router(user_router)                         
