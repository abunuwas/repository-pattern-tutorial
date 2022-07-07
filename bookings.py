from datetime import datetime
from typing import Optional


class Booking:
    def __init__(self, restaurant: int, party_size: int, date_time: datetime, booking_id: Optional[int] = None, booking_record=None):
        self.restaurant = restaurant
        self.party_size = party_size
        self.date_time = date_time
        self._id = booking_id
        self._booking_record = booking_record

    @property
    def id(self):
        return self._id or self._booking_record.id

    def dict(self):
        return {
            "booking_id": self.id,
            "restaurant": self.restaurant,
            "party_size": self.party_size,
            "date_time": self.date_time,
        }
