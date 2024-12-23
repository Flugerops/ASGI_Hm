from contextlib import asynccontextmanager

from fastapi import FastAPI

from .ws_manager import ConnectionManager


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.connection_manager = ConnectionManager()
    yield
