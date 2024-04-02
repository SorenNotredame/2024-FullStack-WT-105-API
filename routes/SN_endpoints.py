# Notredame Sören
from fastapi import APIRouter
import database
from queries import SN_queries as queries
from models import SN_models as models

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


@app.get('/webshop')
def get_webshop_beer_info():
    query = queries.webshop_beers_query
    beers = database.execute_sql_query(query)
    if isinstance(beers, Exception):
        return beers, 500
    beers_to_return = []
    for beer in beers:
        beers_to_return.append({
            "name": beer[0],
            "id": beer[1],
            "text": beer[2],
            "bottle": beer[3],
            "crate": beer[4],
            "image": beer[5]
        })
    return {'beers': beers_to_return}


@app.post("/order")
def create_order(order: models.Orders):
    query = queries.webshop_insert_order
    success = database.execute_sql_query(query, (
        order.name,
        order.total,
        order.date,
    ))
    if success:
        return order


@app.post("/order_beers")
def create_order_beers(order_beers: models.OrderBeers):
    query = queries.webshop_insert_beers_order
    success = database.execute_sql_query(query, (
        order_beers.ordersId,
        order_beers.beer,
        order_beers.bottles,
        order_beers.crates,
    ))
    if success:
        return order_beers


@app.get("/get_order_id")
def get_order_id(name: str):
    query = queries.get_orders_id
    order = database.execute_sql_query(query, (name,))
    if isinstance(order, Exception):
        return order, 500
    return {"orderId": order[0][0]}
