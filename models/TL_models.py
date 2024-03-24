# Author: Tony Ledoux
from pydantic import BaseModel
from datetime import date

class Faq(BaseModel):
    question: str | None = None
    awnser: str | None = None
    asked_by: str | None = None
    awnsered_by: str | None = None
    complete: bool = False
