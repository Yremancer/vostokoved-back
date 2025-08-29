from fastapi import APIRouter
from .routers.dialog_rout import dialog_router


api_controller = APIRouter()
api_controller.include_router(dialog_router, prefix='/dialog', tags=['Dialog'])

