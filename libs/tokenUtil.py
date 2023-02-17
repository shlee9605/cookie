import os
from datetime import timedelta, datetime
from jose import jwt

from fastapi import HTTPException, Header

# make token at login
def makeToken(user_id):
    # 1. Make Token
    data = {
        "sub": user_id,
        "exp": datetime.utcnow()+timedelta(minutes=int(os.environ["ACCESS_TOKEN_EXPIRE_MINUTES"]))
    }
    if not data["sub"] or not data["exp"]:
        raise HTTPException(status_code=500, detail="Create Token Failed")

    # 2. Return JWT Token Encoded
    try:
        return jwt.encode(data, os.environ["SECRET_KEY"], algorithm=os.environ["ALGORITHM"])
    except:
        raise HTTPException(status_code=500, detail="Create Token Failed")

# verify token at calls
async def verifyToken(authorization = Header(None)):
    # 1. Check Request Header
    if not authorization:
        raise HTTPException(status_code=401, detail="Authorization header is missing")
    
    # 2. Check Token Type
    token_type, token = authorization.split()
    if token_type != os.environ["TOKEN_TYPE"]:
        raise HTTPException(status_code=401, detail="Invalid token type")
    
    # 3. Verify Token
    try:
        payload = jwt.decode(token, os.environ["SECRET_KEY"], algorithms=[os.environ["ALGORITHM"]])
    except:
        raise HTTPException(status_code=401, detail="Invalid token")
    
    # 4. Response
    return payload

# def verifyToken(token):
#     token = token.split(os.environ["TOKEN_TYPE"]+" ")[1]
#     params = jwt.decode(token, os.environ["SECRET_KEY"], os.environ["ALGORITHM"])
#     return params

