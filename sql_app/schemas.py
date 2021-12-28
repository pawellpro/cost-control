from datetime import datetime

from pydantic import BaseModel


class Item(BaseModel):
    time: datetime
    category: str
    price: float
    owner_id: int

    class Config:
        orm_mode = True


class User(BaseModel):
    id: int
    login: str
    password: str
    balance: float
    items: list[Item] = []

    class Config:
        orm_mode = True
