# Author: Tony Ledoux
get_open_questions = "SELECT question,id FROM brusselsbrews.faq WHERE complete = 0;"
get_closed_questions = "SELECT question, awnser FROM brusselsbrews.faq WHERE complete = 1;"
ask_new_question = "INSERT INTO brusselsbrews.faq (question, asked_by) VALUES (%s,%s)"
get_last_ID = "SELECT MAX(id) FROM brusselsbrews.faq;"
awnser_question = "UPDATE brusselsbrews.faq SET awnser = %s, awnsered_by = %s, complete = 1 WHERE id = %s;"
get_question_by_id = "SELECT question, awnser, asked_by, awnsered_by, complete FROM brusselsbrews.faq WHERE id = %s;"
#queries for the jobs section
get_job_titles = "SELECT id, jobtitle FROM brusselsbrews.jobs__titles WHERE still_active = true ORDER BY jobtitle ASC;"
post_job_title = "INSERT INTO brusselsbrews.jobs__titles (jobtitle) VALUES (%s);"
get_job_offers = "SELECT id,(select jobtitle from brusselsbrews.jobs__titles as a WHERE b.jobtitle=a.id) as jobtitle, jobdescription, skills, education, experience, created FROM brusselsbrews.jobs__offers as b WHERE filled = false order by created DESC limit %s offset %s;"
count_job_offers = "SELECT COUNT(*) FROM brusselsbrews.jobs__offers WHERE filled = false;"
post_job_offer = "INSERT INTO brusselsbrews.jobs__offers (jobtitle, jobdescription, skills, education, experience) VALUES (%s,%s,%s,%s,%s);"