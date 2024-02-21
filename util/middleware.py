from fastapi import Header, HTTPException
from typing import Annotated
from util import JWTHandler
import os

jwt_handler = JWTHandler(secret=os.getenv("JWT_SECRET"))

async def check_jwt(authorization: Annotated[str, Header()]):
    if not authorization:
        raise HTTPException(status_code=401, detail="Authorization header not found")
    auth_type, token = authorization.split(" ")
    if auth_type.lower() != "bearer" or not token:
        raise HTTPException(status_code=401, detail="Invalid authorization type")
    
    try:
        user, err = jwt_handler.verify_token(token)
        if err:
            raise HTTPException(status_code=401, detail=err)
        return user
    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e))