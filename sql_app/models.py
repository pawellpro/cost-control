from sqlalchemy import Column, Float, String, DateTime, ForeignKey, Integer
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    login = Column(String, unique=True)
    password = Column(String)
    balance = Column(Float)
    items = relationship("Item", back_populates="owner")


class Item(Base):
    __tablename__ = "items"

    time = Column(DateTime, primary_key=True)
    category = Column(String)
    price = Column(Float)
    owner_id = Column(Integer, ForeignKey('users.id'))

    owner = relationship("User", back_populates="items")
