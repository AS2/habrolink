# Some dummy functions
from passlib.context import CryptContext
import logging

logging.getLogger('passlib').setLevel(logging.ERROR)
password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_hashed_password(password: str) -> str:
    return password_context.hash(password)


def verify_password(password: str, hashed_pass: str) -> bool:
    return password_context.verify(password, hashed_pass)


from datetime import datetime, timedelta
from typing import Union, Any
from jose import jwt


JWT_ACCESS_TOKEN_SECRET = "please_please_update_me_please_1"
JWT_REFRESH_TOKEN_SECRET = "please_please_update_me_please_2"

JWT_ACCESS_TOKEN_EXPIRE_MINUTES = 10
JWT_REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24

JWT_ALGORITHM = "HS256"


def create_access_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    if expires_delta is not None:
        expires_delta = datetime.now() + expires_delta
    else:
        expires_delta = datetime.now() + timedelta(minutes=JWT_ACCESS_TOKEN_EXPIRE_MINUTES)
    
    to_encode = {"exp": expires_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, JWT_ACCESS_TOKEN_SECRET, JWT_ALGORITHM)
    return encoded_jwt

def create_refresh_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    if expires_delta is not None:
        expires_delta = datetime.now() + expires_delta
    else:
        expires_delta = datetime.now() + timedelta(minutes=JWT_REFRESH_TOKEN_EXPIRE_MINUTES)
    
    to_encode = {"exp": expires_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, JWT_REFRESH_TOKEN_SECRET, JWT_ALGORITHM)
    return encoded_jwt


from fastapi import HTTPException, status
from pydantic import ValidationError

def get_user_id_by_token(token: str) -> int:
    try:
        token_data = jwt.decode(token, JWT_ACCESS_TOKEN_SECRET, JWT_ALGORITHM)
        
        if datetime.fromtimestamp(token_data["exp"]) < datetime.now():
            raise HTTPException(
                status_code = status.HTTP_401_UNAUTHORIZED,
                detail="Token expired",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except(jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return int(token_data["sub"])

from fastapi.security import OAuth2PasswordBearer

reuseable_oauth = OAuth2PasswordBearer(
    tokenUrl="/user/signin",
    scheme_name="JWT"
)