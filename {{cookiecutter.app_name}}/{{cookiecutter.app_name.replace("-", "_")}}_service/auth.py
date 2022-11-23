import os
import sys
from typing import Optional

import requests
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from jose import JWTError, jwt
from jose.constants import ALGORITHMS
from pydantic import BaseModel


class TokenData(BaseModel):
    username: Optional[str] = None


class User(BaseModel):
    username: str


try:
    r = requests.get(os.getenv("JWT_ISSUER") if os.getenv("JWT_ISSUER") else "http://192.168.1.119:8080/auth/realms/master",
                     timeout=3)
    r.raise_for_status()
    response_json = r.json()
except requests.exceptions.HTTPError as errh:
    print("Http Error:", errh)
    sys.exit(1)
except requests.exceptions.ConnectionError as errc:
    print("Error Connecting:", errc)
    sys.exit(1)
except requests.exceptions.Timeout as errt:
    print("Timeout Error:", errt)
    sys.exit(1)
except requests.exceptions.RequestException as err:
    print("OOps: Something Else", err)
    sys.exit(1)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
SECRET_KEY = f'-----BEGIN PUBLIC KEY-----\r\n{response_json["public_key"]}\r\n-----END PUBLIC KEY-----'


async def get_auth(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHMS.RS256],
                             options={"verify_signature": True, "verify_aud": False, "exp": True})
        username: str = payload.get("preferred_username")
        token_data = TokenData(username=username)
    except JWTError as e:
        print(e)
        raise credentials_exception
    return token_data


async def get_user(current_user: User = Depends(get_auth)):
    return current_user
