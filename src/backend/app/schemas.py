from pydantic import BaseModel, Field
from typing import List, Optional
from enum import IntEnum
from fastapi import Query
from dataclasses import dataclass

def genOpenAPIExample(data, isRequired = False):
        return {
            "normal": {"summary": "Normal request example", "value": data}
        }

# Enum for deciding from where this person came
class PersonSourceEnum(IntEnum):
    HABR = 0
    HABROLINKER = 1


# base class for info from all responses
class CommonResponse(BaseModel):
    token: str = Field(default="token")  # authentication token or empty string


# class which represent info about 1 person
class Person(BaseModel):
    id: str = Field(default="Big_bro")                                             # person identifier
    source: PersonSourceEnum = Field(default=PersonSourceEnum.HABROLINKER)         # source of this person entry.
    fullname: str = Field(default="Артур Шелби")                                   # shown name
    avatar: str = Field(default="https://someimage.org/img.png")                   # link to avatar
    gender: int = Field(default=1)                                                 # gender of person. 0 - woman, 1 - man
    birthday: str = Field(default="1880-01-20")                                    # birthday in postgres-style
    location_country: str = Field(default="Англия")                                # location country
    location_region: str = Field(default="Смоллхит")                               # location region
    location_city: str = Field(default="Бирмингем")                                # location city
    salary: int = Field(default=90000000)                                          # desired salary
    habr_rating: int = Field(default=49)                                           # rating on habr if presented
    habr_karma: int = Field(default=140)                                           # karma on habr if presented
    specialities: List[str] = Field(default=["Рэкетирство", "Общение с клиентами"])  # list of specialities
    skills: List[str] = Field(default=["Писать", "Считать", "Боксировать", "Софтскилс"])  # list of skills


# Response when 1 person needed
class PersonResponse(CommonResponse, Person):
    pass

# parameters for searching
@dataclass
class PersonSearchArguments:
    page: Optional[int] = Query(default=None, openapi_examples=genOpenAPIExample(0))
    source: Optional[PersonSourceEnum] = Query(default=None, openapi_examples=genOpenAPIExample(PersonSourceEnum.HABROLINKER))
    habr_rating_low: Optional[int] = Query(default=None, openapi_examples=genOpenAPIExample(0))
    habr_rating_high: Optional[int] = Query(default=None, openapi_examples=genOpenAPIExample(100))
    habr_karma_low: Optional[int] = Query(default=None, openapi_examples=genOpenAPIExample(0))
    habr_karma_high: Optional[int] = Query(default=None, openapi_examples=genOpenAPIExample(100))
    age_low: Optional[int] = Query(default=None, openapi_examples=genOpenAPIExample(0))
    age_high: Optional[int] = Query(default=None, openapi_examples=genOpenAPIExample(99))
    location_country: Optional[str] = Query(default=None, openapi_examples=genOpenAPIExample("Англия"))
    location_city: Optional[str] = Query(default=None, openapi_examples=genOpenAPIExample("Смоллхит"))
    location_region: Optional[str] = Query(default=None, openapi_examples=genOpenAPIExample("Бирмингем"))
    salary_low: Optional[int] = Query(default=None, openapi_examples=genOpenAPIExample(0))
    salary_high: Optional[int] = Query(default=None, openapi_examples=genOpenAPIExample(999999999999))
    skills: Optional[str] = Query(default=None, openapi_examples=genOpenAPIExample("Рэкетирство,Общение с клиентами"))
    speciality: Optional[str] = Query(default=None, openapi_examples=genOpenAPIExample("Писать"))


# parameters for searching
class PersonSearchResponse(CommonResponse):
    page : int = Field(default=0)                                        # current page
    pages_amount : int = Field(default=1)                                # number of pages
    persons_ids: List[str] = Field(default=[], examples=[["Big_bro"]]) # list with persons ids

