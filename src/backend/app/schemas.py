from pydantic import BaseModel, Field
from typing import List, Optional
from enum import IntEnum


#######
# TYPES
#######

# Enum for deciding from where this person came
class PersonSourceEnum(IntEnum):
    HABR = 0
    HABROLINKER = 1


# class which represent info about 1 person
class Person(BaseModel):
    id: str = Field(default="Big_bro")  # person identifier
    source: PersonSourceEnum = Field(default=PersonSourceEnum.HABROLINKER)  # source of this person entry.
    fullname: str = Field(default="Артур Шелби")  # shown name
    avatar: str = Field(default="https://someimage.org/img.png")  # link to avatar
    gender: int = Field(default=1)  # gender of person. 0 - woman, 1 - man
    birthday: str = Field(default="1880-01-20")  # birthday in postgres-style
    location_country: str = Field(default="Англия")  # location country
    location_region: str = Field(default="Смоллхит")  # location region
    location_city: str = Field(default="Бирмингем")  # location city
    salary: int = Field(default=90000000)  # desired salary
    habr_rating: int = Field(default=49)  # rating on habr if presented
    habr_karma: int = Field(default=140)  # karma on habr if presented
    specialities: List[str] = Field(default=["Рэкетирство", "Общение с клиентами"])  # list of specialities
    skills: List[str] = Field(default=["Писать", "Считать", "Боксировать", "Софтскилс"])  # list of skills


# class which represent info about 1 user
class User(BaseModel):
    id: int = Field(default=0)                                   # user identifier
    login: str = Field(default="soft_kitty_lover@mail.com")      # login of this user
    person_id: str = Field(default="Big_bro")                    # person_id for this user entry


class ChatShortInfo(BaseModel):
    user_id: int       # user we are talking to
    avatar: str        # avatar for this chat
    name: str          # drawn name

class Message(BaseModel):
    from_id: int       # from who message sent
    to_id: int         # to who message sent
    message: str       # text of the message

#######
# COMMON CLASSES
#######


# base class for info from all responses
class CommonResponse(BaseModel):
    pass


# base class for info from all requests
class CommonArguments(BaseModel):
    pass


#######
# ARGUMENTS SCHEMAS
#######

# in case arguments is just 1 user
class UserIdArguments(CommonArguments):
    user_id: int

    @staticmethod
    def get_example():
        return {
            "short": {
                "summary": "Shortest valid example",
                "value": {
                    "user_id": 0
                }
            },
            "normal": {
                "summary": "Biggest valid example",
                "value": {
                    "user_id": 0
                }
            }
        }


# in case arguments is just 1 person
class PersonIdArguments(CommonArguments):
    person_id: str

    @staticmethod
    def get_example():
        return {
            "short": {
                "summary": "Shortest valid example",
                "value": {
                    "person_id": "Big_bro"
                }
            },
            "normal": {
                "summary": "Biggest valid example",
                "value": {
                    "person_id": "Big_bro"
                }
            }
        }


# parameters for searching
class PersonSearchArguments(CommonArguments):
    page: Optional[int] = Field(default=None)
    source: Optional[PersonSourceEnum] = Field(default=None)
    habr_rating_low: Optional[int] = Field(default=None)
    habr_rating_high: Optional[int] = Field(default=None)
    habr_karma_low: Optional[int] = Field(default=None)
    habr_karma_high: Optional[int] = Field(default=None)
    age_low: Optional[int] = Field(default=None)
    age_high: Optional[int] = Field(default=None)
    location_country: Optional[str] = Field(default=None)
    location_city: Optional[str] = Field(default=None)
    location_region: Optional[str] = Field(default=None)
    salary_low: Optional[int] = Field(default=None)
    salary_high: Optional[int] = Field(default=None)
    skills: List[str] = Field(default=[])
    speciality: List[str] = Field(default=[])

    @staticmethod
    def get_example():
        return {
            "short": {
                "summary": "Shortest valid example",
                "value": {
                }
            },
            "normal": {
                "summary": "Biggest valid example",
                "value": {
                    "page": 0,
                    "source": PersonSourceEnum.HABROLINKER,
                    "habr_rating_low": 0,
                    "habr_rating_high": 100,
                    "habr_karma_low": 0,
                    "habr_karma_high": 100,
                    "age_low": 0,
                    "age_high": 99,
                    "location_country": "Англия",
                    "location_city": "Смоллхит",
                    "location_region": "Бирмингем",
                    "salary_low": 0,
                    "salary_high": 999999999999,
                    "skills": ["Рэкетирство", "Общение с клиентами"],
                    "speciality": ["Писать"]
                }
            }
        }


# arguments for Marking API
class MarkingArguments(CommonArguments):
    person_id: str                      # index of person we want to operate on

    @staticmethod
    def get_example():
        return {
            "short": {
                "summary": "Shortest valid example",
                "value": {
                    "person_id" : "Big_bro"
                }
            },
            "normal": {
                "summary": "Biggest valid example",
                "value": {
                    "person_id" : "Big_bro"
                }
            }
        }


class UserSignupArguments(BaseModel):
    login: str = Field(...)
    password: str = Field(...)

    class Config:
        json_schema_extra = {
            "example": {
                "login": "abdulazeez@x.com",
                "password": "weakpassword"
            }
        }


class UserSigninArguments(BaseModel):
    login: str = Field(...)
    password: str = Field(...)

    class Config:
        json_schema_extra = {
            "example": {
                "login": "abdulazeez@x.com",
                "password": "weakpassword"
            }
        }


class PersonCreateUpdateArguments(BaseModel):
    fullname: str = Field(default="Артур Шелби")  # shown name
    avatar: str = Field(default="https://someimage.org/img.png")  # link to avatar
    gender: int = Field(default=1)  # gender of person. 0 - woman, 1 - man
    birthday: str = Field(default="1880-01-20")  # birthday in postgres-style
    location_country: str = Field(default="Англия")  # location country
    location_region: str = Field(default="Смоллхит")  # location region
    location_city: str = Field(default="Бирмингем")  # location city
    salary: int = Field(default=90000000)  # desired salary
    specialities: List[str] = Field(default=["Рэкетирство", "Общение с клиентами"])  # list of specialities
    skills: List[str] = Field(default=["Писать", "Считать", "Боксировать", "Софтскилс"])  # list of skills

    @staticmethod
    def get_example():
        return {
            "normal": {
                "summary": "Valid example",
                "value": {
                    "fullname": "Артур Шелби",
                    "avatar": "https://someimage.org/img.png",
                    "gender": 1,
                    "birthday": "1880-01-20",
                    "location_country": "Англия",
                    "location_region": "Смоллхит",
                    "location_city": "Бирмингем",
                    "salary": 90000000,
                    "specialities": ["Рэкетирство", "Общение с клиентами"],
                    "skills": ["Писать", "Считать", "Боксировать", "Софтскилс"],
                }
            }
        }


class MessageSendArguments(BaseModel):
    user_id: int  # user we want to send message to
    message: str  # message we want to send

    @staticmethod
    def get_example():
        return {
            "normal": {
                "summary": "Valid example",
                "value": {
                    "user_id": 1,
                    "message": "Артур, нужна твоя помощь. Приезжай в паб."
                }
            }
        }


#######
# RESPONSE SCHEMAS
#######

# Response when 1 person needed
class PersonResponse(CommonResponse, Person):
    pass


# Response when 1 user info needed
class UserResponse(CommonResponse, User):
    pass


# Response when user id needed
class UserIdResponse(CommonResponse):
    user_id: int = Field(default=0)


# parameters for searching
class PersonSearchResponse(CommonResponse):
    page: int = Field(default=0)  # current page
    pages_amount: int = Field(default=1)  # number of pages
    persons_ids: List[str] = Field(default=[], examples=[["Big_bro"]])  # list with persons ids


# arguments for Marking API
class MarkListResponse(CommonResponse):
    persons_ids: List[str] = Field(default=[], examples=[["Big_bro"]])  # index of marked persons

# arguments for Marking API
class MarkStatusResponse(CommonResponse):
    status: int = Field(default=0, examples=[0, 1])                     # marked or not


class PersonCreateLinkUpdateResponse(CommonResponse):
    user_id: int = Field(default=0, examples=[1])
    person_id: str = Field(default="", examples=["Big_bro"])


class UserSigninResponse(BaseModel):
    access_token: str = Field(...)
    refresh_token: str = Field(...)

    class Config:
        json_schema_extra = {
            "example": {
                "access_token": "ewtrhyuthdghty",
                "refresh_token": "yrtutjhtyghdfh"
            }
        }


class UserSignupResponse(BaseModel):

    class Config:
        json_schema_extra = {
            "example": {
            }
        }


class MessageChatsResponse(BaseModel):
    chats: List[ChatShortInfo] = Field(default=[], examples=[
        [
            {
                "chat_id": "Big_bro",
                "avatar": "https://someimage.org/img.png",
                "fullname": "Артур Шелби"
            },
            {
                "chat_id": "Lil_bro",
                "avatar": "https://someimage.org/img.png",
                "fullname": "Джон Шелби",
            }
        ]
    ])  # List with all, current user chats

class MessageDialogResponse(BaseModel):
    this_user_id: int = Field(default=0, examples=[1])
    this_user_name: str = Field(default="", examples=["Томас Шелби"])
    this_user_avatar: str = Field(default="", examples=["https://someimage.org/img.png"])
    other_user_id: int = Field(default=0, examples=[0])
    other_user_name: str = Field(default="", examples=["Артур Шелби"])
    other_user_avatar: str = Field(default="", examples=["https://someimage.org/img.png"])
    messages: List[Message] = Field(default=[], examples=[[
        [
            {
                "from_id": 1,
                "to_id": 0,
                "message": "Артур, нужна твоя помощь.\nПриезжай в паб."
            },
            {
                "from_id": 0,
                "to_id": 1,
                "message": "Хорошо, Том. Скоро буду."
            },
            {
                "from_id": 0,
                "to_id": 1,
                "message": "Ой, Томми, прости. Сорвался, сообщение от злости удалил. Напиши еще раз, куда подъехать :*."
            }
        ]
    ]])

