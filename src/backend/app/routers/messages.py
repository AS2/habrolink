from fastapi import APIRouter
from typing import Annotated

from fastapi import APIRouter, HTTPException, Body, Depends
from ..authentication import get_user_id_by_token, reuseable_oauth
from ..config import DBConfig, SEARCH_ENTRIES_PER_PAGE, NONE_PERSON_MARK, UNKNOWN_AVATAR, UNKNOWN_USER

from ..schemas import UserIdArguments, MessageSendArguments, MessageChatsResponse, ChatShortInfo, MessageDialogResponse, \
    Message
import psycopg2

router = APIRouter()


@router.get("/message/chats", tags=["message"], summary="List all chats between current user and other users")
async def list_chats(token: str = Depends(reuseable_oauth)) -> MessageChatsResponse:
    # connect to DB
    conn = psycopg2.connect(
        host=DBConfig["host"],
        database=DBConfig["database"],
        user=DBConfig["user"],
        password=DBConfig["password"],
        port=DBConfig["port"])

    if conn.closed:
        raise HTTPException(status_code=500, detail="Cannot connect to database")

    result = MessageChatsResponse()

    # if token for user not valid this function will throw an exception
    user_id = get_user_id_by_token(token)

    try:
        with conn.cursor() as cur:
            cur.execute('SELECT DISTINCT "chats"."user_id" FROM ('
                        '  (SELECT DISTINCT "message"."from" AS "user_id" FROM "message" WHERE "message"."to" = %s)'
                        '  UNION '
                        '  (SELECT DISTINCT "message"."to" AS "user_id" FROM "message" WHERE "message"."from" = %s)'
                        ') AS "chats"', (user_id, user_id))
            entries = cur.fetchall()
            for i in range(len(entries)):
                chat_id = entries[i][0]
                # get corresponding person
                cur.execute('SELECT "user"."person_id", "user"."login" FROM "user" WHERE "user"."id" = %s', (user_id,))
                entry = cur.fetchone()
                if entry is None:
                    # We do not have opponent in this dialog. Let-s put some dummy info
                    result.chats.append(ChatShortInfo(user_id=chat_id, avatar=UNKNOWN_AVATAR, name=UNKNOWN_USER))
                elif entry[0] == NONE_PERSON_MARK:
                    # We have dialog with user without person_id. Let-s put some dummy info
                    result.chats.append(ChatShortInfo(user_id=chat_id, avatar=UNKNOWN_AVATAR, name=entry[1]))
                else:
                    person_id = entry[0]
                    user_login = entry[1]
                    cur.execute('SELECT "person"."fullname", "person"."avatar" FROM "person" WHERE "person"."id" = %s',
                                (person_id,))
                    entry = cur.fetchone()
                    if entry is None:
                        # Something is wrong with person_id. Let-s put some dummy info
                        result.chats.append(ChatShortInfo(user_id=chat_id, avatar=UNKNOWN_AVATAR, name=user_login))
                    else:
                        # Put valid data
                        result.chats.append(ChatShortInfo(user_id=chat_id, avatar=entry[1], name=entry[0]))

    except psycopg2.OperationalError:
        raise HTTPException(status_code=500, detail="Cannot retrieve data from database")
    conn.close()
    return result


@router.post("/message/send", tags=["message"], summary="Send a message to another user")
async def send_message(
        arguments: Annotated[MessageSendArguments, Body(openapi_examples=MessageSendArguments.get_example())],
        token: str = Depends(reuseable_oauth)):
    # connect to DB
    conn = psycopg2.connect(
        host=DBConfig["host"],
        database=DBConfig["database"],
        user=DBConfig["user"],
        password=DBConfig["password"],
        port=DBConfig["port"])

    if conn.closed:
        raise HTTPException(status_code=500, detail="Cannot connect to database")

    # if token for user not valid this function will throw an exception
    this_user_id = get_user_id_by_token(token)

    try:
        with conn.cursor() as cur:
            # retrieve chat history
            cur.execute('INSERT INTO "message" ("from", "to", "message") VALUES (%s, %s, %s)',
                        (this_user_id, arguments.user_id, arguments.message))
    except psycopg2.OperationalError:
        raise HTTPException(status_code=500, detail="Cannot retrieve data from database")
    conn.commit()
    conn.close()
    return


@router.get("/message/dialog", tags=["message"], summary="List all messages between current user and other user")
async def dialog_chats(arguments: Annotated[UserIdArguments, Body(openapi_examples=UserIdArguments.get_example())],
                     token: str = Depends(reuseable_oauth)) -> MessageDialogResponse:
    # connect to DB
    conn = psycopg2.connect(
        host=DBConfig["host"],
        database=DBConfig["database"],
        user=DBConfig["user"],
        password=DBConfig["password"],
        port=DBConfig["port"])

    if conn.closed:
        raise HTTPException(status_code=500, detail="Cannot connect to database")

    result = MessageDialogResponse()

    # if token for user not valid this function will throw an exception
    this_user_id = get_user_id_by_token(token)

    try:
        with conn.cursor() as cur:
            # fill info about this user
            result.this_user_id = this_user_id
            cur.execute('SELECT "user"."person_id", "user"."login" FROM "user" WHERE "user"."id" = %s',
                        (result.this_user_id,))
            entry = cur.fetchone()
            if entry is None:
                # no use entry... strange but ok
                result.this_user_name = UNKNOWN_USER
                result.this_user_avatar = UNKNOWN_AVATAR
            else:
                person_id = entry[0]
                user_login = entry[1]
                cur.execute('SELECT "person"."fullname", "person"."avatar" FROM "person" WHERE "person"."id" = %s',
                            (person_id,))
                entry = cur.fetchone()
                if entry is None:
                    # no person, lets put dummy values
                    result.this_user_name = user_login
                    result.this_user_avatar = UNKNOWN_AVATAR
                else:
                    result.this_user_name = entry[0]
                    result.this_user_avatar = entry[1]

            # fill info about other user
            result.other_user_id = arguments.user_id
            cur.execute('SELECT "user"."person_id", "user"."login" FROM "user" WHERE "user"."id" = %s',
                        (result.other_user_id,))
            entry = cur.fetchone()
            if entry is None:
                # no use entry... strange but ok
                result.other_user_name = UNKNOWN_USER
                result.other_user_avatar = UNKNOWN_AVATAR
            else:
                person_id = entry[0]
                user_login = entry[1]
                cur.execute('SELECT "person"."fullname", "person"."avatar" FROM "person" WHERE "person"."id" = %s',
                            (person_id,))
                entry = cur.fetchone()
                if entry is None:
                    # no person, lets put dummy values
                    result.other_user_name = user_login
                    result.other_user_avatar = UNKNOWN_AVATAR
                else:
                    result.other_user_name = entry[0]
                    result.other_user_avatar = entry[1]

            # fill info about messages
            cur.execute('SELECT * FROM "message" WHERE '
                        '("message"."from" = %s AND "message"."to" = %s)'
                        ' OR '
                        '("message"."from" = %s AND "message"."to" = %s)', (this_user_id, arguments.user_id, arguments.user_id, this_user_id,))
            entries = cur.fetchall()
            entries.sort(key=lambda x: x[0]) ## sort them by time
            for i in range(len(entries)):
                result.messages.append(Message(from_id=entries[i][1], to_id=entries[i][2], message=entries[i][3]))

    except psycopg2.OperationalError:
        raise HTTPException(status_code=500, detail="Cannot retrieve data from database")
    conn.close()
    return result
