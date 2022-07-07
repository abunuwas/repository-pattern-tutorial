from fastapi import FastAPI

from api import router


def create_server(session_maker=None, repositories=None):
    server = FastAPI(debug=True)
    server.include_router(router)
    server.session_maker = session_maker
    server.repositories = repositories
    return server
