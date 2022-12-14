"""Main FastApi Endpoints"""
import fastapi
# Libraries
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import messages
# Modules
from config import config
from server import ServerFastApiFactory
from views.berry import berry_view
from views.berry_matplot import html


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=config.CORS_ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
server_factory = ServerFastApiFactory()


@app.get("/")
def get_histogram():
    server = server_factory()
    return fastapi.responses.HTMLResponse(html(server))


@app.get(
    "/allBerryStats",
    response_model=messages.PokeApiResponse,
    tags=["Berry Stats"],
    summary="Get Berry Stats",
    status_code=200,
)
def get_all_berries():
    """Get All Berries Statistics"""
    server = server_factory()
    return berry_view.list(server)
