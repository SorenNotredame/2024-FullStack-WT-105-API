# Author: GEBRUERS Stef
from fastapi import APIRouter
import database
from queries import SG_queries as queries
from models import SG_models as models
from datetime import date

today = date.today()
date_string = (today.strftime("%Y-%m-%d"),)
print(type(date_string))


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


@app.post('/contactforms')
def post_contact_form(contactform: models.ContactForm):
    query = queries.submit_new_contactform
    success = database.execute_sql_query(query, (
        contactform.firstName,
        contactform.surName,
        contactform.emailAddress,
        contactform.content,
        contactform.terms,
        contactform.addToMailingList,
        contactform.submitDate,
    ))
    if success:
        return contactform

@app.get('/events')
def get_events(operator : str = ">="):
    if operator == ">=":
        query = queries.get_future_events
    elif operator == "<":
        query = queries.get_past_events
    events = database.execute_sql_query(query, date_string)
    if isinstance(events, Exception):
        return events, 500
    events_to_return = []
    for event in events:
        event_dictionary = {"eventName": event[0],
                               "eventDate": event[1],
                               "eventDescription": event[2],
                               "eventLocation": event[3]}
        print(event_dictionary)
        events_to_return.append(event_dictionary)
    return {'Events': events_to_return}

@app.post('/addevent')
def submit_event(event: models.Event):
    query = queries.submit_new_event
    success = database.execute_sql_query(query, (
        event.eventName,
        event.eventDate,
        event.eventDescription,
        event.eventLocation,
        event.eventPrice,
        event.eventAccepted,
    ))
    if success:
        return event
