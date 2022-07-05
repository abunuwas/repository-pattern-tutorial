from fastapi import FastAPI

from api import router


def create_server():
    server = FastAPI(debug=True)
    server.include_router(router)
    return server
