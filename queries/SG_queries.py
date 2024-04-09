# Author: GEBRUERS Stef

get_all_employeecards = "SELECT employeeId, firstName, alias, firstWords, bio, linkToPicture, bioTitle from brusselsbrews.employee;"

submit_new_contactform = "INSERT INTO brusselsbrews.contactforms (firstName, surName, emailAddress, content, termsAndConditions, addToMailingList, submitDate) VALUES (%s, %s, %s, %s, %s, %s, %s);"