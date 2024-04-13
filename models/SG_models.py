# Author: GEBRUERS Stef

from pydantic import BaseModel
from datetime import datetime


class ContactForm(BaseModel):
    firstName: str
    surName: str
    emailAddress: str
    content: str
    terms: int
    addToMailingList: int = None
    submitDate: datetime

class Event(BaseModel):
    eventName: str
    eventDate: datetime
    eventDescription: str
    eventLocation: str
    eventAccepted: int = 0
