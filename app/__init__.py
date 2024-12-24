from contextlib import asynccontextmanager

from fastapi import FastAPI

# from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware

from .utils import lifespan


app = FastAPI(title=__name__, lifespan=lifespan)
# app.add_middleware(HTTPSRedirectMiddleware) Приклад налаштування безпеки. Потрібен SSL

from . import websockets
