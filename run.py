import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from data_access.repositories_registry import RepositoriesRegistry
from data_access.repository import BookingsRepository
from server import create_server

session_maker = sessionmaker(bind=create_engine(os.getenv("DB_URL")))

repositories_registry = RepositoriesRegistry(bookings_repo=BookingsRepository)

server = create_server(session_maker=session_maker, repositories=repositories_registry)
