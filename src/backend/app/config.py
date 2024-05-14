
DBConfig = {
    "host" : "habrolink_db",
    "database" : "habrolinkdb",
    "user" : "postgres",
    "password" : "12345",
    "port" : "5432"
}

SEARCH_ENTRIES_PER_PAGE = 20

JWT_ACCESS_TOKEN_SECRET = "please_please_update_me_please_1"
JWT_REFRESH_TOKEN_SECRET = "please_please_update_me_please_2"

JWT_ACCESS_TOKEN_EXPIRE_MINUTES = 10
JWT_REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24

JWT_ALGORITHM = "HS256"

NONE_PERSON_MARK = "none"