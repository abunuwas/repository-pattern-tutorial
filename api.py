from datetime import datetime
from typing import List

from fastapi import APIRouter
from pydantic import BaseModel, conint
from starlette import status
from starlette.requests import Request

router = APIRouter()


class BookTable(BaseModel):
    restaurant: int
    party_size: conint(ge=1)
    date_time: datetime


class BookingConfirmation(BaseModel):
    booking_id: int
    restaurant: int
    party_size: int
    date_time: datetime


class BookingsList(BaseModel):
    bookings: List[BookingConfirmation]


@router.get("/bookings", response_model=BookingsList)
def get_bookings(request: Request):
    with request.app.session_maker() as session:
        bookings_repo = request.app.repositories.bookings_repo(session)
        return {
            "bookings": bookings_repo.list()
        }


@router.post("/bookings", status_code=status.HTTP_201_CREATED, response_model=BookingConfirmation)
def book_table(request: Request, booking_details: BookTable):
    with request.app.session_maker() as session:
        bookings_repo = request.app.repositories.bookings_repo(session)
        booking = bookings_repo.add(
            restaurant=booking_details.restaurant,
            party_size=booking_details.party_size,
            date_time=booking_details.date_time
        )
        session.commit()
        return booking.dict()
