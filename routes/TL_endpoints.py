# LEDOUX Tony
from fastapi import APIRouter
import database
from queries import TL_queries as queries
from models import TL_models as models

app = APIRouter()

@app.get("/open_questions")
def get_unanswered_questions():
    query = queries.get_open_questions
    open_questions=database.execute_sql_query(query)
    if isinstance(open_questions, Exception):
        return open_questions, 500
    questions_to_return = []
    for question in open_questions:
        questions_to_return.append({
            "question": question[0],
            "id": question[1],
        })
    return {"open_questions": questions_to_return}

@app.get("/closed_questions")
def get_unanswered_questions():
    query = queries.get_closed_questions
    closed_questions=database.execute_sql_query(query)
    if isinstance(closed_questions, Exception):
        return closed_questions, 500
    questions_to_return = []
    for question in closed_questions:
        questions_to_return.append({
            "question": question[0],
            "answer": question[1],
        })
    return {"closed_questions": questions_to_return}

@app.post("/ask_question")
def ask_question(question: models.Faq):
    query=queries.ask_new_question
    success=database.execute_sql_query(query, (
        question.question,
        question.asked_by,
        ))
    id_query=queries.get_last_ID
    ids=database.execute_sql_query(id_query)
    id=ids[0][0]
    if success:
        r=question.model_dump()
        r["id"]=id
        return r

@app.put("/answer_question/{id}")
def answer_question_with_id(id: int, question: models.Faq):
    # remove the key from the question object is null
    data = question.model_dump()
    for key in list(data):
        if data[key] == None:
            data.pop(key)
    # remove the complete key from the data object
    if "complete" in data:
        data.pop("complete")
    # add the id to the data object
    data["id"] = id
    # see if the id exists
    query = queries.get_question_by_id
    question_data = database.execute_sql_query(query, (id,))
    if question_data == []:
        return {"error": "No question with that id exists."}
    # get params from the dataobject
    awner = data["awnser"]
    awnsered_by = data["awnsered_by"]
    # update the question
    a=queries.awnser_question
    success=database.execute_sql_query(a, (
        awner,
        awnsered_by,
        id,
        ))
    if isinstance(success, Exception):
        return success, 500

    return success