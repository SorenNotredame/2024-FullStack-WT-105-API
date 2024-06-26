# Author: GEBRUERS Stef

get_all_employeecards = "SELECT employeeId, firstName, alias, firstWords, bio, linkToPicture, bioTitle from brusselsbrews.employee;"

submit_new_contactform = "INSERT INTO brusselsbrews.contactforms (firstName, surName, emailAddress, content, termsAndConditions, addToMailingList, submitDate) VALUES (%s, %s, %s, %s, %s, %s, %s);"

get_future_events = "SELECT eventId, eventName, eventDate, eventDescription, eventLocation from brusselsbrews.event where eventDate >= %s and eventAccepted = '1' order by eventDate,eventName;"

get_past_events = "SELECT eventId, eventName, eventDate, eventDescription, eventLocation from brusselsbrews.event where eventDate < %s and eventAccepted = '1' order by eventDate, eventName;"

submit_new_event= "INSERT INTO brusselsbrews.event (eventName, eventDate, eventDescription, eventLocation, eventAccepted) VALUES (%s, %s, %s, %s, %s);"