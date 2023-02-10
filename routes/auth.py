from fastapi import APIRouter, HTTPException, Request, Response

from services import user_service
from libs.tokenUtil import makeToken

router = APIRouter()

TOKEN_TYPE = "Bearer"

# login
@router.post("/kingdom/token", status_code=201)
async def user_root(request: Request, response: Response):
    # 1. Check Request
    try:
        params = await request.json()
    except:
        raise HTTPException(status_code=400, detail="Bad Request")

    # 2. Execute Bussiness Logic
    result = await user_service.login_user(params)

    # 3. Response
    response.headers["token"] = makeToken(result.user_id)
    response.headers["token_type"] = TOKEN_TYPE

    return {
        "token": "certificated",
        "user_id": result.user_id
    }

