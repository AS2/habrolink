from typing import List, Union, Optional
from dataclasses import dataclass

from fastapi import FastAPI, Query, Body, Depends
from pydantic import BaseModel, Field

app = FastAPI()

class UserAuth(BaseModel):
    login: str
    password_hash: str

# User-bounded API
@app.post("/user/auth")
async def user_auth(
    data: UserAuth = Body(
        examples=[
            {
                "login": "tommy1884@mail.com",
                "password_hash": "HashHashHashHash",
            }
        ],
    ),
):
    return {"status": 1, "token" : "abcabcabc"}

class UserRegisterNew(BaseModel):
    login : str
    password_hash : str
    fullname : str
    avatar : str
    gender : int
    birthday : str
    location_country : str
    location_city : str
    location_region : str
    salary : int
    skills : List[str]
    speciality : List[str]

@app.post("/user/registration/new")
async def user_registration(data: UserRegisterNew = Body(
        examples=[
            {
                "login" : "tommy1884@mail.com",
                "password_hash" : "HashHashHashHash",
                "fullname" : "Томас Шелби",
                "avatar" : "https://someimage.org/img.png",
                "gender" : 1,
                "birthday" : "20.01.1884",
                "location_country" : "Англия",
                "location_city" : "Смоллхит",
                "location_region" : "Бирмингем",
                "salary" : 20000000,
                "skills" : ["Скачки", "Гадание", "Софтскиллс"],
                "speciality" : ["Ведение Биснеса"]
            }
        ],
    ),):
    return {"status": 1, "token" : "abcabcabc"}

class UserRegisterHabr(BaseModel):
    login : str
    password_hash : str
    habr_id : str

@app.post("/user/registration/habr")
async def user_registration(data: UserRegisterHabr = Body(
        examples=[
            {
                "login" : "tommy1884@mail.com",
                "password_hash" : "HashHashHashHash",
                "habr_id" : "tshelby",
            }
        ],
    ),):
    return {"status": 1, "token" : "abcabcabc"}

class JustToken(BaseModel):
    token : str

@app.get("/user/info")
async def user_info(data: JustToken = Body(
        examples=[{
                "token": "abcabcabc",
                }]
    )):
    return {
        "fullname": "Томас Шелби",
        "avatar" : "https://someimage.org/img.png",
        "person_id" : "tshelby",
        "login" : "tommy1884@mail.com",
        "gender" : 1,
        "birthday" : "20.01.1884",
        "location_country" : "Англия",
        "location_region" : "Смоллхит",
        "location_city" : "Бирмингем",
        "salary" : 20000000,
        "habr_rating" : 50,
        "habr_karma" : 200,
        "speciality" : ["Ведение Биснеса"],
        "skills" : ["Скачки", "Гадание", "Софтскиллс"]
    }

class UserUpdate(BaseModel):
    token : str
    password_hash : str
    fullname : str
    avatar : str
    gender : int
    birthday : str
    location_country : str
    location_city : str
    location_region : str
    salary : int
    skills : List[str]
    speciality : List[str]

@app.post("/user/update")
async def user_update(data: UserUpdate = Body(
        examples=[
            {
                "token" : "abcabcabc",
                "password_hash" : "HashHashHashHash",
                "fullname" : "Томас Шелби",
                "avatar" : "https://someimage.org/img.png",
                "gender" : 1,
                "birthday" : "20.01.1884",
                "location_country" : "Англия",
                "location_city" : "Смоллхит",
                "location_region" : "Бирмингем",
                "salary" : 20000000,
                "skills" : ["Скачки", "Гадание", "Софтскиллс"],
                "speciality" : ["Ведение Биснеса"]
            }
        ],
    ),):
    return {"status": 1, "token" : "abcabcabc"}

# Messages API

@app.get("/user/messages/chats")
async def user_messages_chats(data: JustToken = Body(
        examples=[{
                "token": "abcabcabc",
                }]
    )):
    return {
        "chats": [
            {
                "chat_id" : "Big_bro",
                "avatar" : "https://someimage.org/img.png",
                "fullname" : "Артур Шелби"
            },
            {
                "chat_id" : "Lil_bro",
                "avatar" : "https://someimage.org/img.png",
                "fullname" : "Джон Шелби"
            },
            {
                "chat_id" : "habrlinker-littlebigman@mail.com",
                "avatar" : "https://someimage.org/img.png",
                "fullname" : "Майкл Грей (Шелби)"
            },
        ]
    }

class UserSendMessage(BaseModel):
    token : str
    chat_id : str
    message : str

@app.post("/user/messages/send")
async def user_messages_send(data: UserSendMessage = Body(
        examples=[{
                "token" : "abcabcabc",
                "chat_id" : "Big_bro",
                "message" : "Артур, нужна твоя помощь. Приезжай в паб."
                }]
    )):
    return {"status": 1}

class UserRefreshMessages(BaseModel):
    token : str
    chat_id : str

@app.get("/user/messages/refresh")
async def user_messages_refresh(data: UserRefreshMessages = Body(
        examples=[{
                "token" : "abcabcabc",
                "chat_id" : "Big_bro",
                }]
    )):
    return {
        "messages": [
            {
                "recieved" : 0,
                "text" : "Артур, нужна твоя помощь. Приезжай в паб"
            },
            {
                "recieved" : 1,
                "text" : "Хорошо, Том. скоро буду."
            },
            {
                "recieved" : 1,
                "text" : "Ой, Томми, прости. Сорвался, сообщение от злости удалил. Напиши еще раз, куда подъехать :*."
            },
        ]
    }

# Persons API

@app.get("/person/info")
async def person_info(person_id : str = Query(
    None,
    openapi_examples={
        "normal" : {
            "summary" : "Example with normal data",
            "value" : "Big_bro"
        }
    }
)):
    return {
        "fullname": "Артур Шелби",
        "avatar" : "https://someimage.org/img.png",
        "person_id" : "Big_bro",
        "login" : "soft_kitty_lover@mail.com",
        "gender" : 1,
        "birthday" : "20.01.1880",
        "location_country" : "Англия",
        "location_region" : "Смоллхит",
        "location_city" : "Бирмингем",
        "salary" : 90000000,
        "habr_rating" : 49,
        "habr_karma" : 140,
        "speciality" : ["Рэкетирство", "Общение с клиентами"],
        "skills" : ["Писать", "Считать", "Боксировать", "Софтскилс"]
    }

@dataclass
class PersonSearch():
    page : Union[int, None] = Query(None, openapi_examples = {"short" : {"summary" : "Short request example", "value" : None}, "full" : {"summary" : "Full request example", "value" : 0}})
    source : Union[int, None] = Query(None, openapi_examples = {"short" : {"summary" : "Short request example", "value" : None}, "full" : {"summary" : "Full request example", "value" : 0}})
    habr_rating_low : Union[int, None] = Query(None, openapi_examples = {"short" : {"summary" : "Short request example", "value" : None}, "full" : {"summary" : "Full request example", "value" : 45}})
    habr_rating_high : Union[int, None] = Query(None, openapi_examples = {"short" : {"summary" : "Short request example", "value" : None}, "full" : {"summary" : "Full request example", "value" : 50}})
    habr_karma_low : Union[int, None] = Query(None, openapi_examples = {"short" : {"summary" : "Short request example", "value" : None}, "full" : {"summary" : "Full request example", "value" : 100}})
    habr_karma_high : Union[int, None] = Query(None, openapi_examples = {"short" : {"summary" : "Short request example", "value" : None}, "full" : {"summary" : "Full request example", "value" : 1000000}})
    age_low : Union[int, None] = Query(None, openapi_examples = {"short" : {"summary" : "Short request example", "value" : None}, "full" : {"summary" : "Full request example", "value" : 0}})
    age_high : Union[int, None] = Query(None, openapi_examples = {"short" : {"summary" : "Short request example", "value" : None}, "full" : {"summary" : "Full request example", "value" : 99}})
    location_country : Union[str, None] = Query(None, openapi_examples = {"short" : {"summary" : "Short request example", "value" : None}, "full" : {"summary" : "Full request example", "value" : "Англия"}})
    location_city : Union[str, None] = Query(None, openapi_examples = {"short" : {"summary" : "Short request example", "value" : None}, "full" : {"summary" : "Full request example", "value" : "Бирмингем"}})
    location_region : Union[str, None] = Query(None, openapi_examples = {"short" : {"summary" : "Short request example", "value" : None}, "full" : {"summary" : "Full request example", "value" : "Смоллхит"}})
    salary_low : Union[int, None] = Query(None, openapi_examples = {"short" : {"summary" : "Short request example", "value" : None}, "full" : {"summary" : "Full request example", "value" : 0}})
    salary_high : Union[int, None] = Query(None, openapi_examples = {"short" : {"summary" : "Short request example", "value" : None}, "full" : {"summary" : "Full request example", "value" : 1000000}})
    skills : Union[List[str], None] = Query(None, openapi_examples = {"short" : {"summary" : "Short request example", "value" : None}, "full" : {"summary" : "Full request example", "value" : ["Рэкетирство"]}})
    speciality : Union[List[str], None] = Query(None, openapi_examples = {"short" : {"summary" : "Short request example", "value" : None}, "full" : {"summary" : "Full request example", "value" : ["Писать", "Считать", "Боксировать"]}})

@app.get("/person/search")
async def person_search(data : PersonSearch = Depends()):
    return {
        "page": 0,
        "pages_amount" : 1,
        "persons" : [
            {
                "fullname" : "Артур Шелби",
                "avatar" : "https://someimage.org/img.png", 
                "source" : 0,
                "person_id" : "Big_bro",
                "habr_karma" : 140,
                "habr_rating" : 49,
                "login" : "soft_kitty_lover@mail.com",
                "marked" : 1
            },
            {
                "fullname" : "Джон Шелби",
                "avatar" : "https://someimage.org/img.png", 
                "source" : 0,
                "person_id" : "Lil_bro",
                "habr_karma" : 124,
                "habr_rating" : 46,
                "login" : "prettygoodboi@mail.com",
                "marked" : 0
            },
            {
                "fullname" : "Майкл Грей (Шелби)",
                "avatar" : "https://someimage.org/img.png", 
                "source" : 1,
                "person_id" : "habrlinker-littlebigman@mail.com",
                "habr_karma" : 0,
                "habr_rating" : 0,
                "login" : "littlebigman@mail.com",
                "marked" : 1
            },
        ]
    }

# Mark API

class PersonMark(BaseModel):
    token : str
    person_id : str

@app.post("/person/marks/add")
async def person_marks_add(data: PersonMark = Body(
        examples = [{
                "token" : "abcabcabc",
                "person_id" : "Big_bro",
                }]
)):
    return {"status": 1}

@app.get("/person/marks/status")
async def person_marks_status(data: PersonMark = Body(
        examples = [{
                "token" : "abcabcabc",
                "person_id" : "Big_bro",
                }]
)):
    return {"marked": 1}

@app.post("/person/marks/remove")
async def person_marks_remove(data: PersonMark = Body(
        examples = [{
                "token" : "abcabcabc",
                "person_id" : "Big_bro",
                }]
)):
    return {"status" : 1}

@app.get("/person/marks/all")
async def person_marks_all(data: JustToken = Body(
        examples=[{
                "token": "abcabcabc",
                }]
    )):
    return {
        "page": 0,
        "pages_amount" : 1,
        "persons" : [
            {
                "fullname" : "Артур Шелби",
                "avatar" : "https://someimage.org/img.png", 
                "source" : 0,
                "person_id" : "Big_bro",
                "habr_karma" : 140,
                "habr_rating" : 49,
                "login" : "soft_kitty_lover@mail.com"
            },
            {
                "fullname" : "Майкл Грей (Шелби)",
                "avatar" : "https://someimage.org/img.png", 
                "source" : 1,
                "person_id" : "habrlinker-littlebigman@mail.com",
                "habr_karma" : 0,
                "habr_rating" : 0,
                "login" : "littlebigman@mail.com"
            },
        ]
    }