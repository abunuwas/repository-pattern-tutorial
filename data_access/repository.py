from bookings import Booking
from data_access.models import Booking as BookingModel


class BookingsRepository:
    def __init__(self, session):
        self.session = session

    def get(self, **filters):
        pass

    def list(self):
        return [
            booking.dict() for booking in self.session.query(BookingModel).all()
        ]

    def add(self, restaurant, date_time, party_size):
        booking = BookingModel(
            restaurant_id=restaurant,
            date_time=date_time,
            party_size=party_size,
        )
        self.session.add(booking)
        return Booking(restaurant=booking.restaurant_id, date_time=booking.date_time, booking_record=booking)

    def update(self, **kwargs):
        pass

    def delete(self, **kwargs):
        pass
