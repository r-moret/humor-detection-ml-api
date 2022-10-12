import uvicorn
from fastapi import FastAPI
from app.api.routes import api_router

app = FastAPI()

app.include_router(router=api_router)

if __name__ == "__main__":
    uvicorn.run("app.main:app", reload=True, host="0.0.0.0", port=80)
