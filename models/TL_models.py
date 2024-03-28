# Author: Tony Ledoux
from pydantic import BaseModel
from datetime import date

class Faq(BaseModel):
    question: str = None
    awnser: str = None
    asked_by: str = None
    awnsered_by: str = None
    complete: bool = False

class JobTitle(BaseModel):
    jobtitle: str = None
    
class Job(BaseModel):
    jobtitle: int = None
    jobdescription: str = None
    skills: str = None
    education: str = None
    experience: str = None