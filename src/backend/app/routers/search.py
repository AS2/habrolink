import math
from typing import Annotated

from fastapi import APIRouter, HTTPException, Body

from ..authentication import update_token, get_user_id_by_token
from ..config import DBConfig, SEARCH_ENTRIES_PER_PAGE
from ..schemas import PersonSearchArguments, PersonSearchResponse, CommonResponse, MarkingArguments, OnlyTokenArguments, \
    MarkListResponse, MarkStatusResponse

import psycopg2

router = APIRouter()


@router.post("/search", response_model=PersonSearchResponse)
async def person_search(searchArguments: Annotated[
    PersonSearchArguments, Body(openapi_examples=PersonSearchArguments.get_example())]) -> PersonSearchResponse:
    # connect to DB
    conn = psycopg2.connect(
        host=DBConfig["host"],
        database=DBConfig["database"],
        user=DBConfig["user"],
        password=DBConfig["password"],
        port=DBConfig["port"])

    if conn.closed:
        raise HTTPException(status_code=500, detail="Cannot connect to database")

    result = PersonSearchResponse()
    result.token = update_token(searchArguments.token)

    try:
        with conn.cursor() as cur:
            filters = []

            if searchArguments.source is not None:
                filters.append(
                    '("person"."source" = 0 OR "person"."source" = ' + str(searchArguments.source.value) + ')')

            if searchArguments.habr_rating_low is not None and searchArguments.habr_rating_high is not None:
                filters.append('("person"."habr_rating" = 0 OR ("person"."habr_rating" >= ' + str(
                    searchArguments.habr_rating_low) + ' AND "person"."habr_rating" <= ' + str(
                    searchArguments.habr_rating_high) + '))')
            elif searchArguments.habr_rating_low is not None:
                filters.append('("person"."habr_rating" = 0 OR ("person"."habr_rating" >= ' + str(
                    searchArguments.habr_rating_low) + '))')
            elif searchArguments.habr_rating_high is not None:
                filters.append('("person"."habr_rating" = 0 OR ("person"."habr_rating" <= ' + str(
                    searchArguments.habr_rating_high) + '))')

            if searchArguments.habr_karma_low is not None and searchArguments.habr_karma_high is not None:
                filters.append('("person"."habr_karma" = 0 OR ("person"."habr_karma" >= ' + str(
                    searchArguments.habr_karma_low) + ' AND "person"."habr_karma" <= ' + str(
                    searchArguments.habr_karma_high) + '))')
            elif searchArguments.habr_karma_low is not None:
                filters.append('("person"."habr_karma" = 0 OR ("person"."habr_karma" >= ' + str(
                    searchArguments.habr_karma_low) + '))')
            elif searchArguments.habr_karma_high is not None:
                filters.append('("person"."habr_karma" = 0 OR ("person"."habr_karma" <= ' + str(
                    searchArguments.habr_karma_high) + '))')

            if searchArguments.age_low is not None and searchArguments.age_high is not None:
                filters.append(
                    '(date_part(\'year\',age("person"."birthday")) > 100 OR (date_part(\'year\',age("person"."birthday")) >= ' + str(
                        searchArguments.age_low) + ' AND date_part(\'year\',age("person"."birthday")) <= ' + str(
                        searchArguments.habr_rating_high) + '))')
            elif searchArguments.age_low is not None:
                filters.append(
                    '(date_part(\'year\',age("person"."birthday")) > 100 OR (date_part(\'year\',age("person"."birthday")) >= ' + str(
                        searchArguments.age_low) + '))')
            elif searchArguments.age_high is not None:
                filters.append(
                    '(date_part(\'year\',age("person"."birthday")) > 100 OR (date_part(\'year\',age("person"."birthday")) <= ' + str(
                        searchArguments.age_high) + '))')

            if searchArguments.location_country is not None:
                filters.append(
                    '("person"."location_country" = \'\' OR "person"."location_country" = \'' + searchArguments.location_country + '\')')
            if searchArguments.location_region is not None:
                filters.append(
                    '("person"."location_region" = \'\' OR "person"."location_region" = \'' + searchArguments.location_region + '\')')
            if searchArguments.location_city is not None:
                filters.append(
                    '("person"."location_city" = \'\' OR "person"."location_city" = \'' + searchArguments.location_city + '\')')

            if searchArguments.salary_low is not None and searchArguments.salary_high is not None:
                filters.append('("person"."salary" = 0 OR ("person"."salary" >= ' + str(
                    searchArguments.salary_low) + ' AND "person"."salary" <= ' + str(
                    searchArguments.salary_high) + '))')
            elif searchArguments.salary_low is not None:
                filters.append(
                    '("person"."salary" = 0 OR ("person"."salary" >= ' + str(searchArguments.salary_low) + '))')
            elif searchArguments.salary_high is not None:
                filters.append(
                    '("person"."salary" = 0 OR ("person"."salary" <= ' + str(searchArguments.salary_high) + '))')

            request = ""
            if len(searchArguments.skills) > 0 or len(searchArguments.speciality) > 0:
                prerequest = "WITH "
                if len(searchArguments.skills) > 0:
                    prerequest += '"skills" AS (SELECT "person_id" FROM "personToSkill" WHERE '
                    for index, skill in enumerate(searchArguments.skills):
                        prerequest += '"personToSkill"."skill" = \'' + skill + '\''
                        if index != len(searchArguments.skills) - 1:
                            prerequest += " OR "
                        else:
                            prerequest += ")"

                if len(searchArguments.skills) > 0 and len(searchArguments.speciality) > 0:
                    prerequest += ","

                if len(searchArguments.speciality) > 0:
                    prerequest += '"speciality" AS (SELECT "person_id" FROM "personToSpeciality" WHERE '
                    for index, speciality in enumerate(searchArguments.speciality):
                        prerequest += '"personToSpeciality"."speciality" = \'' + speciality + '\''
                        if index != len(searchArguments.speciality) - 1:
                            prerequest += " OR "
                        else:
                            prerequest += ")"

                request = prerequest + ' SELECT "id" FROM "person"'

                if len(searchArguments.skills) > 0:
                    request += ' JOIN "skills" ON "skills"."person_id" = "person"."id"'
                if len(searchArguments.speciality) > 0:
                    request += ' JOIN "speciality" ON "speciality"."person_id" = "person"."id"'

            if len(filters) == 0:
                request += ' GROUP BY "id"'
            else:
                request += ' WHERE ' + ' AND '.join(filters) + ' GROUP BY "id"'

            cur.execute(request)
            entries = cur.fetchall()

            # fill data
            if searchArguments.page is not None:
                result.page = searchArguments.page
            else:
                result.page = 0

            result.pages_amount = int(math.ceil(len(entries) / SEARCH_ENTRIES_PER_PAGE))

            for i in range(result.page * SEARCH_ENTRIES_PER_PAGE,
                           min(len(entries), (result.page + 1) * SEARCH_ENTRIES_PER_PAGE), 1):
                result.persons_ids.append(entries[i][0])

    except psycopg2.OperationalError:
        raise HTTPException(status_code=500, detail="Cannot retrieve data from database")
    conn.close()
    return result


@router.post("/mark/add", response_model=CommonResponse)
async def add_mark(markArguments: Annotated[
    MarkingArguments, Body(openapi_examples=MarkingArguments.get_example())]) -> CommonResponse:
    # connect to DB
    conn = psycopg2.connect(
        host=DBConfig["host"],
        database=DBConfig["database"],
        user=DBConfig["user"],
        password=DBConfig["password"],
        port=DBConfig["port"])

    if conn.closed:
        raise HTTPException(status_code=500, detail="Cannot connect to database")

    result = CommonResponse()
    result.token = update_token(markArguments.token)

    # todo - ensure that user is valid

    try:
        with conn.cursor() as cur:
            cur.execute('INSERT INTO "marked" ("user_id", "person_id") VALUES (%s, %s) ON CONFLICT DO NOTHING',
                        (get_user_id_by_token(result.token), markArguments.person_id))
            cur.commit()
    except psycopg2.OperationalError:
        raise HTTPException(status_code=500, detail="Cannot retrieve data from database")
    conn.close()
    return result


@router.post("/mark/remove", response_model=CommonResponse)
async def remove_mark(markArguments: Annotated[
    MarkingArguments, Body(openapi_examples=MarkingArguments.get_example())]) -> CommonResponse:
    # connect to DB
    conn = psycopg2.connect(
        host=DBConfig["host"],
        database=DBConfig["database"],
        user=DBConfig["user"],
        password=DBConfig["password"],
        port=DBConfig["port"])

    if conn.closed:
        raise HTTPException(status_code=500, detail="Cannot connect to database")

    result = CommonResponse()
    result.token = update_token(markArguments.token)

    # todo - ensure that user is valid

    try:
        with conn.cursor() as cur:
            cur.execute('DELETE FROM "marked" WHERE "user_id" = %s AND "person_id" = %s',
                        (get_user_id_by_token(result.token), markArguments.person_id))
            cur.commit()
    except psycopg2.OperationalError:
        raise HTTPException(status_code=500, detail="Cannot retrieve data from database")
    conn.close()
    return result


@router.post("/mark/list", response_model=MarkListResponse)
async def list_marked(user: Annotated[
    OnlyTokenArguments, Body(openapi_examples=OnlyTokenArguments.get_example())]) -> MarkListResponse:
    # connect to DB
    conn = psycopg2.connect(
        host=DBConfig["host"],
        database=DBConfig["database"],
        user=DBConfig["user"],
        password=DBConfig["password"],
        port=DBConfig["port"])

    if conn.closed:
        raise HTTPException(status_code=500, detail="Cannot connect to database")

    result = MarkListResponse()
    result.token = update_token(user.token)

    # todo - ensure that user is valid

    try:
        with conn.cursor() as cur:
            cur.execute('SELECT "person_id" FROM "marked" WHERE "user_id" = %s', (get_user_id_by_token(result.token),))
            entries = cur.fetchall()
            for i in range(len(entries)):
                result.persons_ids.append(entries[i][0])

    except psycopg2.OperationalError:
        raise HTTPException(status_code=500, detail="Cannot retrieve data from database")
    conn.close()
    return result


@router.post("/mark/status", response_model=MarkListResponse)
async def check_is_marked(markArguments: Annotated[
    MarkingArguments, Body(openapi_examples=MarkingArguments.get_example())]) -> MarkStatusResponse:
    # connect to DB
    conn = psycopg2.connect(
        host=DBConfig["host"],
        database=DBConfig["database"],
        user=DBConfig["user"],
        password=DBConfig["password"],
        port=DBConfig["port"])

    if conn.closed:
        raise HTTPException(status_code=500, detail="Cannot connect to database")

    result = MarkStatusResponse()
    result.token = update_token(markArguments.token)
    result.status = 0

    # todo - ensure that user is valid

    try:
        with conn.cursor() as cur:
            cur.execute('SELECT "person_id" FROM "marked" WHERE "user_id" = %s AND "person_id" = %s',
                        (get_user_id_by_token(result.token), markArguments.person_id))
            entries = cur.fetchall()
            if len(entries) > 0:
                result.status = 1

    except psycopg2.OperationalError:
        raise HTTPException(status_code=500, detail="Cannot retrieve data from database")
    conn.close()
    return result
