from typing import List, Union, Optional
from dataclasses import dataclass

from fastapi import APIRouter, Query, Body, Depends, HTTPException
from pydantic import BaseModel, Field

from ..config import DBConfig

import psycopg2

router = APIRouter()

class PersonInfoResponse(BaseModel):
    fullname : str
    avatar : str
    person_id : str
    login : str
    gender : int
    birthday : str
    location_country : str
    location_region : str
    location_city : str
    salary : int
    habr_rating : int
    habr_karma : int
    speciality : List[str]
    skills : List[str]

@router.get("/person/info")
async def person_info(person_id : str = Query(
    None,
    openapi_examples={
        "normal" : {
            "summary" : "Example with normal data",
            "value" : "Big_bro"
        }
    }
)) -> PersonInfoResponse:
    # connect to DB
    conn = psycopg2.connect(
        host=DBConfig["host"],
        database=DBConfig["database"],
        user=DBConfig["user"],
        password=DBConfig["password"],
        port=DBConfig["port"])
        
    if conn.closed:
        raise HTTPException(status_code=500, detail="Cannot connect to database")        
    
    result = {}
    
    try:
        with conn.cursor() as cur:
            cur.execute('SELECT * FROM "person" WHERE "person"."id" = %s', (person_id,))
            entry = cur.fetchone()
            if entry == None:
                raise HTTPException(status_code=500, detail="No such person")
            result['person_id'] = entry[0]
            result['fullname'] = entry[2]
            result['avatar'] = entry[3]
            result['gender'] = entry[4]
            result['birthday'] = entry[5]
            result['location_country'] = entry[6]
            result['location_region'] = entry[7]
            result['location_city'] = entry[8]
            result['salary'] = entry[9]
            result['habr_rating'] = entry[10]
            result['habr_karma'] = entry[11]
            
            cur.execute('SELECT "personToSkill"."skill" FROM "personToSkill" WHERE "personToSkill"."person_id" = %s', (person_id,))
            entry = cur.fetchall()
            result['skills'] = []
            for el in entry:
                result['skills'].append(el)
            
            cur.execute('SELECT "personToSpeciality"."speciality" FROM "personToSpeciality" WHERE "personToSpeciality"."person_id" = %s', (person_id,))
            result['speciality'] = []
            for el in entry:
                result['speciality'].append(el)
    except psycopg2.OperationalError:
        raise HTTPException(status_code=500, detail="Cannot retrieve data from database")
  
    return result