# Author: Frank Wagemans

from pydantic import BaseModel
from datetime import date

class new_dealer(BaseModel):
    businessname: str
    address: str
    phone: str
    email: str

class tour(BaseModel):
    name: str
    email: str
    phone: str
    date: date
    timeslot: str
    amount: int

class tasting(BaseModel):
    name: str
    address: str
    email: str
    phone: str
    date: date
    amount: int

class new_review(BaseModel):
    new_reviewname: str
    new_reviewtext: str
    new_reviewemail: str
