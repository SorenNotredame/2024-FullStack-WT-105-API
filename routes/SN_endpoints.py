# Notredame Sören
from fastapi import APIRouter
import database
from queries import SN_queries as queries

app = APIRouter()


@app.get('/dropdown')
def get_dropdown_info():
    query = queries.dropdown_query
    dropdown = database.execute_sql_query(query)
    if isinstance(dropdown, Exception):
        return dropdown, 500
    info_to_return = []
    for info in dropdown:
        info_to_return.append({
            "name": info[0],
            "id": info[1],
        })
    return {'dropdown': info_to_return}

@app.get('/beers')
def get_beer_info():
    query = queries.beers_query
    beers = database.execute_sql_query(query)
    if isinstance(beers, Exception):
        return beers, 500
    beers_to_return = []
    for beer in beers:
        beers_to_return.append({
            "name": beer[0],
            "id": beer[1],
            "text": beer[2],
            "allergens": beer[3],
            "image": beer[4]
        })
    return {'beers': beers_to_return}
