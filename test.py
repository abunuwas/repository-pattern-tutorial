import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from starlette.testclient import TestClient

from server import create_server

server = create_server()

test_client = TestClient(app=server)


def test():
    payload = {
        "restaurant": 1,
        "party_size": 1,
        "date_time": "2022-07-14T17:02:01.373Z"
    }
    response = test_client.post('/bookings', json=payload)
    assert response.status_code == 201
