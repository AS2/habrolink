from typing import Annotated

from fastapi import APIRouter, HTTPException, Body, status, Depends
from fastapi.security import OAuth2PasswordRequestForm

from ..authentication import get_hashed_password, create_access_token, create_refresh_token, verify_password, reuseable_oauth, get_user_id_by_token
from ..config import DBConfig, NONE_PERSON_MARK
from ..schemas import PersonResponse, PersonIdArguments, UserIdResponse, UserResponse, UserIdArguments, \
    UserSigninResponse, UserSignupArguments, UserSignupResponse, PersonCreateUpdateArguments, \
    PersonCreateLinkUpdateResponse

import psycopg2

router = APIRouter()


@router.post("/person/info", tags=["person"], summary="Retrieve info about person by person id", response_model=PersonResponse)
async def person_by_id(arguments: Annotated[PersonIdArguments, Body(openapi_examples=PersonIdArguments.get_example())], token: str = Depends(reuseable_oauth)) -> PersonResponse:
    # connect to DB
    conn = psycopg2.connect(
        host=DBConfig["host"],
        database=DBConfig["database"],
        user=DBConfig["user"],
        password=DBConfig["password"],
        port=DBConfig["port"])

    if conn.closed:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Cannot connect to database")

    result = PersonResponse()

    try:
        with conn.cursor() as cur:
            cur.execute('SELECT * FROM "person" WHERE "person"."id" = %s', (arguments.person_id,))
            entry = cur.fetchone()
            if entry == None:
                raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="No such person")
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
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Cannot retrieve data from database")
    conn.close()
    return result

@router.post("/person/create", tags=["person"], summary="Create new person and automatically link it to a user")
async def create_person(arguments: Annotated[PersonCreateUpdateArguments, Body(openapi_examples=PersonCreateUpdateArguments.get_example())], token: str = Depends(reuseable_oauth)) -> PersonCreateLinkUpdateResponse:
    # connect to DB
    conn = psycopg2.connect(
        host=DBConfig["host"],
        database=DBConfig["database"],
        user=DBConfig["user"],
        password=DBConfig["password"],
        port=DBConfig["port"])

    if conn.closed:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Cannot connect to database")

    # if token for user not valid this function will throw an exception
    user_id = get_user_id_by_token(token)
    result = PersonCreateLinkUpdateResponse(user_id=user_id, person_id="habrolinker-" + str(user_id))

    try:
        with conn.cursor() as cur:
            cur.execute('INSERT INTO "person" '
                        '("id",'
                        ' "source",'
                        ' "fullname",'
                        ' "avatar",'
                        ' "gender",'
                        ' "birthday",'
                        ' "location_country",'
                        ' "location_city",'
                        ' "location_region",'
                        ' "salary",'
                        ' "habr_karma",'
                        ' "habr_rating") VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 0, 0)',
                        ("habrolinker-" + str(user_id),
                         1,
                         arguments.fullname,
                         arguments.avatar,
                         arguments.gender,
                         arguments.birthday,
                         arguments.location_country,
                         arguments.location_city,
                         arguments.location_region,
                         arguments.salary))
            # TODO - specialities and skills
            cur.execute('UPDATE "user" SET "person_id" = %s WHERE "user"."id" = %s', ("habrolinker-" + str(user_id), user_id))
    except psycopg2.OperationalError:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Cannot retrieve data from database")
    conn.commit()
    conn.close()
    return result

@router.put("/person/update", tags=["person"], summary="Update person (associated to logged in user) fields")
async def update_person(arguments: Annotated[PersonCreateUpdateArguments, Body(openapi_examples=PersonCreateUpdateArguments.get_example())], token: str = Depends(reuseable_oauth)) -> PersonCreateLinkUpdateResponse:
    # connect to DB
    conn = psycopg2.connect(
        host=DBConfig["host"],
        database=DBConfig["database"],
        user=DBConfig["user"],
        password=DBConfig["password"],
        port=DBConfig["port"])

    if conn.closed:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Cannot connect to database")

    # if token for user not valid this function will throw an exception
    user_id = get_user_id_by_token(token)
    result = PersonCreateLinkUpdateResponse(user_id=user_id, person_id="habrolinker-" + str(user_id))

    try:
        with conn.cursor() as cur:
            # firstly -> get person id
            cur.execute('SELECT "user"."person_id" FROM "user" WHERE "user"."id" = %s', (user_id,))
            entry = cur.fetchone()
            if entry == None or entry[0] == NONE_PERSON_MARK:
                raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="No person for such user")
            result.person_id = entry[0]

            cur.execute('UPDATE "person" SET '
                        '("fullname",'
                        ' "avatar",'
                        ' "gender",'
                        ' "birthday",'
                        ' "location_country",'
                        ' "location_city",'
                        ' "location_region",'
                        ' "salary") = (%s, %s, %s, %s, %s, %s, %s, %s) WHERE "person"."id" = %s',
                        (arguments.fullname,
                         arguments.avatar,
                         arguments.gender,
                         arguments.birthday,
                         arguments.location_country,
                         arguments.location_city,
                         arguments.location_region,
                         arguments.salary, result.person_id))
            # TODO - specialities and skills
    except psycopg2.OperationalError:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="Cannot retrieve data from database")
    conn.commit()
    conn.close()
    return result
@router.post("/person/link", tags=["person"], summary="Link existing to a user")
async def link_person(arguments: Annotated[PersonIdArguments, Body(openapi_examples=PersonIdArguments.get_example())], token: str = Depends(reuseable_oauth)) -> PersonCreateLinkUpdateResponse:
    # connect to DB
    conn = psycopg2.connect(
        host=DBConfig["host"],
        database=DBConfig["database"],
        user=DBConfig["user"],
        password=DBConfig["password"],
        port=DBConfig["port"])

    if conn.closed:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Cannot connect to database")

    # if token for user not valid this function will throw an exception
    user_id = get_user_id_by_token(token)
    result = PersonCreateLinkUpdateResponse(user_id=user_id, person_id="habrolinker-" + str(user_id))

    try:
        with conn.cursor() as cur:
            # firstly -> check if this person id is already taken
            cur.execute('SELECT "user"."id" FROM "user" WHERE "user"."person_id" = %s', (arguments.person_id,))
            entry = cur.fetchone()
            if entry != None:
                raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Already taken")
            result.person_id = arguments.person_id

            cur.execute('UPDATE "user" SET "person_id" = %s WHERE "user"."id" = %s', (arguments.person_id, user_id))
    except psycopg2.OperationalError:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="Cannot retrieve data from database")
    conn.commit()
    conn.close()
    return result

# find user by person_id
@router.post("/user/find", tags=["user"], summary="Retrieve person id for provided user", response_model=UserIdResponse)
async def user_by_person(arguments: Annotated[PersonIdArguments, Body(openapi_examples=PersonIdArguments.get_example())], token: str = Depends(reuseable_oauth)) -> UserIdResponse:
    # connect to DB
    conn = psycopg2.connect(
        host=DBConfig["host"],
        database=DBConfig["database"],
        user=DBConfig["user"],
        password=DBConfig["password"],
        port=DBConfig["port"])

    if conn.closed:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Cannot connect to database")

    result = UserIdResponse()

    try:
        with conn.cursor() as cur:
            cur.execute('SELECT "user"."user_id" FROM "user" WHERE "user"."person_id" = %s', (arguments.person_id,))
            entry = cur.fetchone()
            if entry == None:
                raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="No such user")
            result.user_id = entry[0]

    except psycopg2.OperationalError:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Cannot retrieve data from database")
    conn.close()
    return result

# find user by person_id
@router.post("/user/info", tags=["user"], summary="Retrieve info about user by user id", response_model=UserResponse)
async def user_by_id(arguments: Annotated[UserIdArguments, Body(openapi_examples=UserIdArguments.get_example())], token: str = Depends(reuseable_oauth)) -> UserResponse:
    # connect to DB
    conn = psycopg2.connect(
        host=DBConfig["host"],
        database=DBConfig["database"],
        user=DBConfig["user"],
        password=DBConfig["password"],
        port=DBConfig["port"])

    if conn.closed:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Cannot connect to database")

    result = UserResponse()

    try:
        with conn.cursor() as cur:
            cur.execute('SELECT * FROM "user" WHERE "user"."id" = %s', (arguments.person_id,))
            entry = cur.fetchone()
            if entry == None:
                raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="No such user")
            result.user_id = entry[0]
            result.login = entry[1]
            result.person_id = entry[3]

    except psycopg2.OperationalError:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Cannot retrieve data from database")
    conn.close()
    return result


@router.post("/user/signup", tags=["user"], summary="Create new user with current login and password", response_model=UserSignupResponse)
async def create_user(arguments: UserSignupArguments = Body(...)):
    # connect to DB
    print("signup start")
    conn = psycopg2.connect(
        host=DBConfig["host"],
        database=DBConfig["database"],
        user=DBConfig["user"],
        password=DBConfig["password"],
        port=DBConfig["port"])

    if conn.closed:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Cannot connect to database")

    result = UserSignupResponse()
    
    try:
        with conn.cursor() as cur:
            cur.execute('SELECT * FROM "user" WHERE "user"."login" = %s', (arguments.login,))
            entry = cur.fetchone()
            if entry is not None:
                raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="User with this email already exist"
            )
            user = {
                'login': arguments.login,
                'password_hash': get_hashed_password(arguments.password),
                'person_id': NONE_PERSON_MARK
            }
        with conn.cursor() as cur:
            cur.execute('INSERT INTO "user" ("id", "login", "password_hash", "person_id") VALUES (DEFAULT, %s, %s, DEFAULT)', (user["login"], user["password_hash"]))

    except psycopg2.OperationalError:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Cannot retrieve data from database")
    print("precommit")
    conn.commit()
    conn.close()
    return result


@router.post('/user/signin', tags=["user"], summary="Create access and refresh tokens for user", response_model=UserSigninResponse)
async def login(arguments: OAuth2PasswordRequestForm = Depends()):
    # connect to DB
    conn = psycopg2.connect(
        host=DBConfig["host"],
        database=DBConfig["database"],
        user=DBConfig["user"],
        password=DBConfig["password"],
        port=DBConfig["port"])

    if conn.closed:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Cannot connect to database")
    try:
        with conn.cursor() as cur:
            cur.execute('SELECT * FROM "user" WHERE "user"."login" = %s', (arguments.username,))
            entry = cur.fetchone()
            if entry is None:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Incorrect email or password"
                )
            password_hash = entry[2]
            if not verify_password(arguments.password, password_hash):
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Incorrect email or password"
                )
            user = {
                'id': entry[0],
                'login': entry[1],
                'password_hash': entry[2],
                'person_id': entry[3]
            }

    except psycopg2.OperationalError:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Cannot retrieve data from database")
    conn.close()
    return UserSigninResponse(access_token=create_access_token(user['id']), refresh_token=create_refresh_token(user['id']))


@router.post('/user/self', tags=["user"], summary="Retrieve info about logged in user", response_model=UserResponse)
async def get_current_user(token: str = Depends(reuseable_oauth)) -> UserResponse:
    user_id = get_user_id_by_token(token)
        
    conn = psycopg2.connect(
        host=DBConfig["host"],
        database=DBConfig["database"],
        user=DBConfig["user"],
        password=DBConfig["password"],
        port=DBConfig["port"])

    if conn.closed:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Cannot connect to database")
    try:
        with conn.cursor() as cur:
            cur.execute('SELECT * FROM "user" WHERE "user"."id" = %s', (user_id,))
            entry = cur.fetchone()
            if entry is None:
                raise HTTPException(
                    status_code=status.HTTP_404_BAD_REQUEST,
                    detail="Could not find user"
                )
            person_id = entry[3]
            if person_id is None:
                person_id = NONE_PERSON_MARK
            user = UserResponse(
                id=entry[0],
                login=entry[1],
                person_id=person_id,
                token=token
            )

    except psycopg2.OperationalError:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Cannot retrieve data from database")
    conn.close()
    return user