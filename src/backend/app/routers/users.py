from fastapi import APIRouter, Query, HTTPException

from ..config import DBConfig
from ..schemas import PersonResponse, genOpenAPIExample

import psycopg2

router = APIRouter()
@router.get("/person", response_model=PersonResponse)
async def person_by_id(person_id: str = Query(None, openapi_examples=genOpenAPIExample("Big_bro"))) -> PersonResponse:
    # connect to DB
    conn = psycopg2.connect(
        host=DBConfig["host"],
        database=DBConfig["database"],
        user=DBConfig["user"],
        password=DBConfig["password"],
        port=DBConfig["port"])

    if conn.closed:
        raise HTTPException(status_code=500, detail="Cannot connect to database")

    result = PersonResponse()
    result.token = ""

    try:
        with conn.cursor() as cur:
            cur.execute('SELECT * FROM "person" WHERE "person"."id" = %s', (person_id,))
            entry = cur.fetchone()
            if entry == None:
                raise HTTPException(status_code=500, detail="No such person")
            result.id = entry[0]
            result.fullname = entry[2]
            result.avatar = entry[3]
            result.gender = entry[4]
            result.birthday = entry[5]
            result.location_country = entry[6]
            result.location_region = entry[7]
            result.location_city = entry[8]
            result.salary = entry[9]
            result.habr_rating = entry[10]
            result.habr_karma = entry[11]

            cur.execute('SELECT "personToSkill"."skill" FROM "personToSkill" WHERE "personToSkill"."person_id" = %s',
                        (person_id,))
            entry = cur.fetchall()
            result.skills = []
            for el in entry:
                result.skills.append(el)

            cur.execute(
                'SELECT "personToSpeciality"."speciality" FROM "personToSpeciality" WHERE '
                '"personToSpeciality"."person_id" = %s',
                (person_id,))
            result.specialities = []
            for el in entry:
                result.specialities.append(el)
    except psycopg2.OperationalError:
        raise HTTPException(status_code=500, detail="Cannot retrieve data from database")
    conn.close()
    return result
