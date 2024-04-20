from typing import Annotated

from fastapi import APIRouter, HTTPException, Body

from ..authentication import update_token
from ..config import DBConfig
from ..schemas import PersonResponse, PersonIdArguments, UserIdResponse, UserResponse, UserIdArguments

import psycopg2

router = APIRouter()


@router.post("/person/info", response_model=PersonResponse)
async def person_by_id(arguments: Annotated[PersonIdArguments, Body(openapi_examples=PersonIdArguments.get_example())]) -> PersonResponse:
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
    result.token = update_token(arguments.token)

    try:
        with conn.cursor() as cur:
            cur.execute('SELECT * FROM "person" WHERE "person"."id" = %s', (arguments.person_id,))
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
                        (arguments.person_id,))
            entry = cur.fetchall()
            result.skills = []
            for el in entry:
                result.skills.append(el)

            cur.execute(
                'SELECT "personToSpeciality"."speciality" FROM "personToSpeciality" WHERE '
                '"personToSpeciality"."person_id" = %s',
                (arguments.person_id,))
            result.specialities = []
            for el in entry:
                result.specialities.append(el)
    except psycopg2.OperationalError:
        raise HTTPException(status_code=500, detail="Cannot retrieve data from database")
    conn.close()
    return result


# find user by person_id
@router.post("/user/find", response_model=UserIdResponse)
async def user_by_person(arguments: Annotated[PersonIdArguments, Body(openapi_examples=PersonIdArguments.get_example())]) -> UserIdResponse:
    # connect to DB
    conn = psycopg2.connect(
        host=DBConfig["host"],
        database=DBConfig["database"],
        user=DBConfig["user"],
        password=DBConfig["password"],
        port=DBConfig["port"])

    if conn.closed:
        raise HTTPException(status_code=500, detail="Cannot connect to database")

    result = UserIdResponse()
    result.token = update_token(arguments.token)

    try:
        with conn.cursor() as cur:
            cur.execute('SELECT "user"."user_id" FROM "user" WHERE "user"."person_id" = %s', (arguments.person_id,))
            entry = cur.fetchone()
            if entry == None:
                raise HTTPException(status_code=500, detail="No such user")
            result.user_id = entry[0]

    except psycopg2.OperationalError:
        raise HTTPException(status_code=500, detail="Cannot retrieve data from database")
    conn.close()
    return result

# find user by person_id
@router.post("/user/info", response_model=UserResponse)
async def user_by_id(arguments: Annotated[UserIdArguments, Body(openapi_examples=UserIdArguments.get_example())]) -> UserResponse:
    # connect to DB
    conn = psycopg2.connect(
        host=DBConfig["host"],
        database=DBConfig["database"],
        user=DBConfig["user"],
        password=DBConfig["password"],
        port=DBConfig["port"])

    if conn.closed:
        raise HTTPException(status_code=500, detail="Cannot connect to database")

    result = UserResponse()
    result.token = update_token(arguments.token)

    try:
        with conn.cursor() as cur:
            cur.execute('SELECT * FROM "user" WHERE "user"."id" = %s', (arguments.person_id,))
            entry = cur.fetchone()
            if entry == None:
                raise HTTPException(status_code=500, detail="No such user")
            result.user_id = entry[0]
            result.login = entry[1]
            result.person_id = entry[3]

    except psycopg2.OperationalError:
        raise HTTPException(status_code=500, detail="Cannot retrieve data from database")
    conn.close()
    return result