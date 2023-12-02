from typing import List

from fastapi import FastAPI, Query

app = FastAPI()

# User-bounded API
@app.get("/user/auth")
async def user_auth(login : str = "", password_hash : str = ""):
    return {"status": 1, "token" : "abcabcabc"}

@app.get("/user/registration/new")
async def user_registration(login : str, password_hash : str, fullname : str, avatar : str, gender : int, birthday : str, location_country : str, location_city : str, location_region : str, salary : int, skills : List[str] = Query(None), speciality : List[str] = Query(None)):
    return {"status": 1, "token" : "abcabcabc"}

@app.get("/user/registration/habr")
async def user_registration(login : str, password_hash : str, habr_id : str):
    return {"status": 1, "token" : "abcabcabc"}

@app.get("/user/info")
async def user_info(token : str):
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

@app.get("/user/update")
async def user_update(token : str, password_hash : str, fullname : str, avatar : str, gender : int, birthday : str, location_country : str, location_city : str, location_region : str, salary : int, skills : List[str] = Query(None), speciality : List[str] = Query(None)):
    return {"status": 1, "token" : "abcabcabc"}

# Messages API

@app.get("/user/messages/chats")
async def user_messages_chats(token : str):
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

@app.get("/user/messages/send")
async def user_messages_send(token : str, chat_id : str, message : str):
    return {"status": 1}

@app.get("/user/messages/refresh")
async def user_messages_refresh(token : str, chat_id : str):
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
async def person_info(person_id : str):
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


@app.get("/person/search")
async def person_search(page : int, source : int, habr_rating_low : int, habr_rating_high : int, habr_karma_low : int, habr_karma_high : int, age_low : int, age_high : int, location_country : str, location_city : str, location_region : str, salary_low : int, salary_high : int,  skills : List[str] = Query(None), speciality : List[str] = Query(None)):
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

@app.get("/person/marks/add")
async def person_marks_add(token : str, person_id : str):
    return {"status": 1}

@app.get("/person/marks/status")
async def person_marks_status(token : str, person_id : str):
    return {"marked": 1}

@app.get("/person/marks/remove")
async def person_marks_remove(token : str, person_id : str):
    return {"status" : 1}

@app.get("/person/marks/all")
async def person_marks_all(token : str):
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