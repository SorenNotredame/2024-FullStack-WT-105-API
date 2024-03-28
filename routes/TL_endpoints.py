# LEDOUX Tony
from fastapi import APIRouter
import database
from queries import TL_queries as queries
from models import TL_models as models

app = APIRouter()


@app.get("/open_questions")
def get_unanswered_questions():
    query = queries.get_open_questions
    open_questions = database.execute_sql_query(query)
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
    closed_questions = database.execute_sql_query(query)
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
    query = queries.ask_new_question
    success = database.execute_sql_query(query, (
        question.question,
        question.asked_by,
    ))
    id_query = queries.get_last_ID
    ids = database.execute_sql_query(id_query)
    id = ids[0][0]
    if success:
        r = question.model_dump()
        r["id"] = id
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
    a = queries.awnser_question
    success = database.execute_sql_query(a, (
        awner,
        awnsered_by,
        id,
    ))
    if isinstance(success, Exception):
        return success, 500

    return success

# Endpoint for jobs section


@app.get("/jobtitles")
def get_jobtitles():
    query = queries.get_job_titles
    jobtitles = database.execute_sql_query(query)
    if isinstance(jobtitles, Exception):
        return jobtitles, 500
    jobtitles_to_return = []
    for jobtitle in jobtitles:
        jobtitles_to_return.append({
            "id": jobtitle[0],
            "jobtitle": jobtitle[1],
        })
    return jobtitles_to_return


@app.get("/joboffers")
def get_joboffers(limit: int = 6, offset: int = 0):
    query = queries.get_job_offers
    result = database.execute_sql_query(query, (limit, offset))
    if isinstance(result, Exception):
        return result, 500
    joboffers_to_return = []
    for joboffer in result:
        joboffers_to_return.append({
            "id": joboffer[0],
            "jobtitle": joboffer[1],
            "jobdescription": joboffer[2],
            "jobRequirements": {
                "skills": joboffer[3],
                "education": joboffer[4],
                "experience": joboffer[5],
            },
            "posted": joboffer[6],
        })
    count_query = queries.count_job_offers
    count = database.execute_sql_query(count_query)
    if isinstance(count, Exception):
        return count, 500
    total = count[0][0]
    admin = {}
    admin["total"] = total
    admin["joboffers"] = joboffers_to_return

    #joboffers_to_return.append({"total": count[0][0]});

    return admin

@app.get("/joboffers/filtered")
def get_filterd_job_offers(filter: str = None, limit: int = 6, offset: int = 0):
    #no filters send all job offers
    if filter == None:
        return get_joboffers(limit, offset)
    #filter by job title
    #convert filter to list
    filter = filter.split(",")
    # for each filter create a query part
    query_parts = []
    for i in range(len(filter)):
        query_parts.append("jobtitle = %s")
    #join the query parts with OR
    query_parts = " OR ".join(query_parts)
    main_query = queries.get_job_offers
    order_and_limit = " ORDER BY created DESC LIMIT %s OFFSET %s;"
    #remove the order and limit from the main query
    main_query = main_query[:-1 * len(order_and_limit)]
    #add a space to the end of the main query
    main_query += " AND (" + query_parts + ")" + order_and_limit
    result = database.execute_sql_query(main_query, filter + [limit, offset])
    if isinstance(result, Exception):
        return result, 500
    #count the total number of job offers in the filter
    count_query = "SELECT COUNT(*) FROM brusselsbrews.jobs__offers WHERE filled = false AND (" + query_parts + ");"
    runed_count_query = database.execute_sql_query(count_query, filter)
    if isinstance(runed_count_query, Exception):
        return runed_count_query, 500
    res_to_return = {}
    res_to_return["total"] = runed_count_query[0][0]
    joboffers=[]
    for joboffer in result:
        joboffers.append({
            "id": joboffer[0],
            "jobtitle": joboffer[1],
            "jobdescription": joboffer[2],
            "jobRequirements": {
                "skills": joboffer[3],
                "education": joboffer[4],
                "experience": joboffer[5],
            },
            "posted": joboffer[6],
        })
    res_to_return["joboffers"] = joboffers
    return res_to_return
    
    


@app.post("/jobtitles")
def post_jobtitle(jobtitle: models.JobTitle):
    query = queries.post_job_title
    success = database.execute_sql_query(query, (
        jobtitle.jobtitle,
    ))
    if isinstance(success, Exception):
        return success, 500
    return success


@app.post("/joboffers")
def add_job(job: models.Job):
    query = queries.post_job_offer
    success = database.execute_sql_query(query, (
        job.jobtitle,
        job.jobdescription,
        job.skills,
        job.education,
        job.experience,
    ))
    if isinstance(success, Exception):
        return success, 500
    return success

@app.delete("/joboffers/{id}")
def delete_job_offer(id: int):
    query = "UPDATE `brusselsbrews`.`jobs__offers` SET `filled` = '1' WHERE (`id` = %s);"
    success = database.execute_sql_query(query, (id,))
    if isinstance(success, Exception):
        return success, 500
    return success