from contextlib import asynccontextmanager

from fastapi import FastAPI

from .utils import lifespan


app = FastAPI(title=__name__, lifespan=lifespan)


from . import websockets
