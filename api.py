import os
from datetime import datetime
from typing import List

from fastapi import APIRouter
from pydantic import BaseModel, conint
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from starlette import status

from data_access.models import Booking

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


session_maker = sessionmaker(bind=create_engine(os.getenv("DB_URL")))


@router.get("/bookings", response_model=BookingsList)
def get_bookings():
    with session_maker() as session:
        bookings = session.query(Booking).all()
        return {
            "bookings": [booking.dict() for booking in bookings]
        }


@router.post("/bookings", status_code=status.HTTP_201_CREATED, response_model=BookingConfirmation)
def book_table(booking_details: BookTable):
    with session_maker() as session:
        booking = Booking(
                restaurant_id=booking_details.restaurant,
                date_time=booking_details.date_time,
                party_size=booking_details.party_size,
            )
        session.add(booking)
        session.commit()
        return {
            "booking_id": booking.id,
            "restaurant": booking_details.restaurant,
            "party_size": booking.party_size,
            "date_time": booking.date_time,
        }
