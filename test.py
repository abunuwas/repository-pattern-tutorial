from unittest.mock import MagicMock

from starlette.testclient import TestClient

from bookings import Booking
from data_access.repositories_registry import RepositoriesRegistry
from server import create_server


class DummyBookingsRepo:
    def __init__(self, _):
        self.bookings = []

    def add(self, restaurant, date_time, party_size):
        booking = Booking(restaurant=restaurant, date_time=date_time, party_size=party_size, booking_id=1)
        self.bookings.append(booking)
        return booking


server = create_server(session_maker=MagicMock(), repositories=RepositoriesRegistry(bookings_repo=DummyBookingsRepo))

test_client = TestClient(app=server)


def test():
    payload = {
        "restaurant": 1,
        "party_size": 1,
        "date_time": "2022-07-14T17:02:01.373Z"
    }
    response = test_client.post('/bookings', json=payload)
    assert response.status_code == 201
