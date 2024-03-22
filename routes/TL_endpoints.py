# LEDOUX Tony
from fastapi import APIRouter
import database
from queries import TL_queries as queries

app = APIRouter()

@app.get("/questions")
def get_questions():
    return {"Hello World"}