from fastapi import APIRouter, HTTPException, Request, Depends
from models.users import Users

from services import user_service

from libs.tokenUtil import verifyToken

router = APIRouter()

# add user
@router.post("/kingdom/user", status_code=201)
async def user_root(request: Users):
    # 1. Check Request
    try:
        params = Users(
            user_id=request.user_id,
            pass_word=request.pass_word,
            year=request.year,
            deletedAt=request.deletedAt
        )
    except:
        raise HTTPException(status_code=400, detail="Bad Request")

    # 2. Execute Bussiness Logic
    response = await user_service.input_user(params)

    # 3. Response
    return response


# get user info
@router.get("/kingdom/user")
async def user_root(param: str, auth = Depends(verifyToken)):
    # 1. Check Request
    try:
        params = param  # get query
    except:
        raise HTTPException(status_code=400, detail="Bad Request")
    
    # 2. Execute Bussiness Logic
    response = await user_service.output_user(params)

    # 3. Response
    return response


# delete user
@router.delete("/kingdom/user")
async def user_root(request: Request, auth = Depends(verifyToken)):
    # 1. Check Request
    try:
        params = await request.json()  # json to dictionary type
        params = params['user_id']
    except:
        raise HTTPException(status_code=400, detail="Bad Request")

    # 2. Execute Bussiness Logic
    response = await user_service.erase_user(params)

    # 3. Response
    return response


# get current user
@router.get("/kingdom/user/current")
async def get_current_user(auth = Depends(verifyToken)):
    # 1. Check Request
    try:
        params: str = auth.get("sub")
        print(params)
    except:
        raise HTTPException(status_code=400, detail="Bad Request")

    # 2. Execute Buissiness Logic
    response = await user_service.output_user(params)

    # 3. Response
    return response
