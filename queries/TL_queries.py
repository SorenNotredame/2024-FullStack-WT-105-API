# Author: Tony Ledoux
get_open_questions = "SELECT question,id FROM brusselsbrews.faq WHERE complete = 0;"
get_closed_questions = "SELECT question, awnser FROM brusselsbrews.faq WHERE complete = 1;"
ask_new_question = "INSERT INTO brusselsbrews.faq (question, asked_by) VALUES (%s,%s)"
get_last_ID = "SELECT MAX(id) FROM brusselsbrews.faq;"
awnser_question = "UPDATE brusselsbrews.faq SET awnser = %s, awnsered_by = %s, complete = 1 WHERE id = %s;"
get_question_by_id = "SELECT question, awnser, asked_by, awnsered_by, complete FROM brusselsbrews.faq WHERE id = %s;"