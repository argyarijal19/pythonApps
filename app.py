import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from routes.user_router import auth
from helper.exception import ExceptionHandler
from starlette_exporter import PrometheusMiddleware, handle_metrics

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

app.add_middleware(PrometheusMiddleware)
app.add_route("/metrics", handle_metrics)
app.include_router(auth)
