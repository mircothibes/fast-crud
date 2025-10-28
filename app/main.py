from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.database import Base, engine
from app.routers.users import router as users_router


app = FastAPI(title="fast-crud")

# Temporary: create tables at startup
Base.metadata.create_all(bind=engine)

# === Global error handlers ===
@app.exception_handler(ValueError)
def value_error_handler(_: Request, exc: ValueError):
    return JSONResponse(status_code=400, content={"detail": str(exc)})


@app.exception_handler(LookupError)
def lookup_error_handler(_: Request, exc: LookupError):
    return JSONResponse(status_code=404, content={"detail": str(exc)})


# === Routes ===
@app.get("/")
def read_root():
    return {"message":"🔥 fast-crud hot-reload is working!"}


@app.get("/health")
def health():
    return {"stuts": "ok"}


# Routers
app.include_router(users_router)












