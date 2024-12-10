from sqlalchemy import Column, Integer, String, DateTime
from app.db.base import Base
from app.db.mixins import TimeSampedMixin
from datetime import datetime


class User(Base, TimeSampedMixin):
    __table__name = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)