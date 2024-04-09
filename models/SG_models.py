# Author: GEBRUERS Stef

from pydantic import BaseModel
from datetime import date


class ContactForm(BaseModel):
    firstName: str
    surName: str
    emailAddress: str
    content: str
    terms: int
    addToMailingList: int
    submitDate: date
