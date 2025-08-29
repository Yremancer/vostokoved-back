from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.api import api_controller
from config import ORIGINS

app = FastAPI()

app.add_middleware (
    CORSMiddleware,
    allow_origins=ORIGINS,
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True
)

app.include_router(api_controller)

