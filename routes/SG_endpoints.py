# GEBRUERS Stef
from fastapi import APIRouter
import database
from queries import SG_queries as queries

app = APIRouter()


@app.get('/employeecards')
def get_all_employeescards():
    query = queries.get_all_employeecards
    carddata = database.execute_sql_query(query)
    if isinstance(carddata, Exception):
        return carddata, 500
    carddata_to_return = []
    for card in carddata:
        employee_dictionary = {"name": card[1],
                               "alias": card[2],
                               "firstWords": card[3],
                               "bio": card[4],
                               "linktoPicture": card[5],
                               "bioTitle": card[6]}
        carddata_to_return.append(employee_dictionary)
    return {'Employeecards': carddata_to_return}
