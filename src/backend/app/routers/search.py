import math

from fastapi import APIRouter, Depends, HTTPException

from ..config import DBConfig, SEARCH_ENTRIES_PER_PAGE
from ..schemas import PersonSearchArguments, PersonSearchResponse

import psycopg2

router = APIRouter()
@router.get("/search", response_model=PersonSearchResponse)
async def person_search(searchArguments: PersonSearchArguments = Depends()) -> PersonSearchResponse:
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
    result.token = ""

    try:
        with conn.cursor() as cur:
            filters = []

            #TODO skills and speciality support

            if searchArguments.source is not None:
                filters.append('("person"."source" = 0 OR "person"."source" = ' + str(searchArguments.source.value) + ')')

            if searchArguments.habr_rating_low is not None and searchArguments.habr_rating_high is not None:
                filters.append('("person"."habr_rating" = 0 OR ("person"."habr_rating" >= ' + str(searchArguments.habr_rating_low) + ' AND "person"."habr_rating" <= ' + str(searchArguments.habr_rating_high) + '))')
            elif searchArguments.habr_rating_low is not None:
                filters.append('("person"."habr_rating" = 0 OR ("person"."habr_rating" >= ' + str(searchArguments.habr_rating_low) + '))')
            elif searchArguments.habr_rating_high is not None:
                filters.append('("person"."habr_rating" = 0 OR ("person"."habr_rating" <= ' + str(searchArguments.habr_rating_high) + '))')

            if searchArguments.habr_karma_low is not None and searchArguments.habr_karma_high is not None:
                filters.append('("person"."habr_karma" = 0 OR ("person"."habr_karma" >= ' + str(searchArguments.habr_karma_low) + ' AND "person"."habr_karma" <= ' + str(searchArguments.habr_karma_high) + '))')
            elif searchArguments.habr_karma_low is not None:
                filters.append('("person"."habr_karma" = 0 OR ("person"."habr_karma" >= ' + str(searchArguments.habr_karma_low) + '))')
            elif searchArguments.habr_karma_high is not None:
                filters.append('("person"."habr_karma" = 0 OR ("person"."habr_karma" <= ' + str(searchArguments.habr_karma_high) + '))')

            if searchArguments.age_low is not None and searchArguments.age_high is not None:
                filters.append('(date_part(\'year\',age("person"."birthday")) > 100 OR (date_part(\'year\',age("person"."birthday")) >= ' + str(searchArguments.age_low) + ' AND date_part(\'year\',age("person"."birthday")) <= ' + str(searchArguments.habr_rating_high) + '))')
            elif searchArguments.age_low is not None:
                filters.append('(date_part(\'year\',age("person"."birthday")) > 100 OR (date_part(\'year\',age("person"."birthday")) >= ' + str(searchArguments.age_low) + '))')
            elif searchArguments.age_high is not None:
                filters.append('(date_part(\'year\',age("person"."birthday")) > 100 OR (date_part(\'year\',age("person"."birthday")) <= ' + str(searchArguments.age_high) + '))')

            if searchArguments.location_country is not None:
                filters.append('("person"."location_country" = \'\' OR "person"."location_country" = \'' + searchArguments.location_country + '\')')
            if searchArguments.location_region is not None:
                filters.append('("person"."location_region" = \'\' OR "person"."location_region" = \'' + searchArguments.location_region + '\')')
            if searchArguments.location_city is not None:
                filters.append('("person"."location_city" = \'\' OR "person"."location_city" = \'' + searchArguments.location_city + '\')')

            if searchArguments.salary_low is not None and searchArguments.salary_high is not None:
                filters.append('("person"."salary" = 0 OR ("person"."salary" >= ' + str(searchArguments.salary_low) + ' AND "person"."salary" <= ' + str(searchArguments.salary_high) + '))')
            elif searchArguments.salary_low is not None:
                filters.append('("person"."salary" = 0 OR ("person"."salary" >= ' + str(searchArguments.salary_low) + '))')
            elif searchArguments.salary_high is not None:
                filters.append('("person"."salary" = 0 OR ("person"."salary" <= ' + str(searchArguments.salary_high) + '))')

            if len(filters) == 0:
                request = 'SELECT "id" FROM "person" GROUP BY "id"'
            else:
                request = 'SELECT "id" FROM "person" WHERE ' + ' AND '.join(filters) + ' GROUP BY "id"'
            print(request)
            cur.execute(request)
            entries = cur.fetchall()

            # fill data
            if searchArguments.page is not None:
                result.page = searchArguments.page
            else:
                result.page = 0

            result.pages_amount = int(math.ceil(len(entries) / SEARCH_ENTRIES_PER_PAGE))

            for i in range(result.page * SEARCH_ENTRIES_PER_PAGE, len(entries), 1):
                result.persons_ids.append(entries[i][0])

    except psycopg2.OperationalError:
        raise HTTPException(status_code=500, detail="Cannot retrieve data from database")
    conn.close()
    return result
