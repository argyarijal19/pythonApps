import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from routes.user_router import auth
from helper.exception import ExceptionHandler

load_dotenv()

app = FastAPI(
    title="Backend For Inventory App - API"
)

ExceptionHandler(app=app)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth)
