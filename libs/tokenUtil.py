import os
from datetime import timedelta, datetime
from jose import jwt

def makeToken(user_id):
    data = {
        "sub": user_id,
        "exp": datetime.utcnow()+timedelta(minutes=int(os.environ["ACCESS_TOKEN_EXPIRE_MINUTES"]))
    }
    return jwt.encode(data, os.environ["SECRET_KEY"], algorithm=os.environ["ALGORITHM"])
