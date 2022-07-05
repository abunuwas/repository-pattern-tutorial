from datetime import datetime

from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Booking(Base):
    __tablename__ = "booking"

    id = Column(Integer, primary_key=True)
    created = Column(DateTime, nullable=False, default=datetime.utcnow)
    restaurant_id = Column(Integer, nullable=False)
    date_time = Column(DateTime, nullable=False)
    party_size = Column(Integer, nullable=False)

    def dict(self):
        return {
            "booking_id": self.id,
            "created": self.created,
            "restaurant": self.restaurant_id,
            "date_time": self.date_time,
            "party_size": self.party_size,
        }
