# Author: Sören Notredame
from pydantic import BaseModel
from datetime import datetime


class Orders(BaseModel):
    name: str
    total: float
    date: datetime


class OrderBeers(BaseModel):
    ordersId: int
    beer: str
    bottles: int
    crates: int

