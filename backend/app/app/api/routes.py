from fastapi import APIRouter
from app.api.endpoints import ModelAPI

router = APIRouter()

model_api = ModelAPI()

router.add_api_route(
    path="/predict", endpoint=model_api.predict, response_model=float, methods=["POST"]
)
