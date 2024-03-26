# WAGEMANS Frank
from fastapi import APIRouter
import database
from queries import FW_queries as queries
from models import FW_models

app = APIRouter()

### Become a dealer
@app.post("/new_dealer")
def create_newdealer(new_dealer: FW_models.new_dealer):
    query = queries.insert_dealer_query
    success = database.execute_sql_query(query, (
        new_dealer.businessname,
        new_dealer.address,
        new_dealer.phone,
        new_dealer.email,
    ))
    if success:
        return new_dealer

### Dealer information
@app.get("/dealerinfo")
def get_dealerinfo():
    query = queries.dealerinfo_query
    dealers = database.execute_sql_query(query)
    if isinstance(dealers, Exception):
        return dealers, 500
    dealer_list = []
    for dealer in dealers:
        dealer_dict = {'dealername': dealer[0], 'streetAndNumber': dealer[1], 'postal_codeAndCity': dealer[2], 'phone': dealer[3], 'email': dealer[4], 'opening_hours': dealer[5], 'products': dealer[6]}
        dealer_list.append(dealer_dict)
    return dealer_list

### Book a tour
@app.post("/tour")
def create_tour(tour: FW_models.tour):
    query = queries.insert_tour_query
    success = database.execute_sql_query(query, (
        tour.name,
        tour.email,
        tour.phone,
        tour.date,
        tour.timeslot,
        tour.amount,
    ))
    if success:
        return tour

### Book a tasting
@app.post("/tasting")
def create_tasting(tasting: FW_models.tasting):
    query = queries.insert_tasting_query
    success = database.execute_sql_query(query, (
        tasting.name,
        tasting.address,
        tasting.email,
        tasting.phone,
        tasting.date,
        tasting.amount,
    ))
    if success:
        return tasting

### Brewer information
@app.get("/brewerinfo")
def get_brewerinfo():
    query = queries.brewerinfo_query
    brewer = database.execute_sql_query(query)
    if isinstance(brewer, Exception):
        return brewer, 500
    brewer_list = []
    for brewer in brewer:
        brewer_dict = {'brewername': brewer[0], 'streetAndNumber': brewer[1], 'postal_codeAndCity': brewer[2], 'phone': brewer[3],'email': brewer[4],'opening_hours': brewer[5],'about': brewer[6]}
        brewer_list.append(brewer_dict)
    return brewer_list

### Author names
@app.get("/authors")
def get_authors():
    query = queries.author_query
    authors = database.execute_sql_query(query)
    if isinstance(authors, Exception):
        return authors, 500
    author_list = []
    for author in authors:
        author_dict = {'authorname': author[0]}
        author_list.append(author_dict)
    return author_list

### Tour timeslots
@app.get("/timeslots")
def get_timeslots():
    query = queries.brewerinfo_query
    brewer = database.execute_sql_query(query)
    if isinstance(brewer, Exception):
        return brewer, 500
    timeslots = []
    for brewer in brewer:
        brewer_dict = {'timeslots': brewer[6]}
        timeslots.append(brewer_dict)
    return timeslots