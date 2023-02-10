from fastapi import APIRouter, HTTPException, Request
from models.users import Users

from services import user_service

router = APIRouter()

# add user
@router.post("/kingdom/user", status_code=201)
async def user_root(request: Users):
    # 1. Check Request
    try:
        params = Users(
            user_id=request.user_id,
            pass_word=request.pass_word,
            year=request.year
        )
    except:
        raise HTTPException(status_code=400, detail="Bad Request")

    # 2. Execute Bussiness Logic
    response = await user_service.input_user(params)

    # 3. Response
    return response


# get user info
@router.get("/kingdom/user")
async def user_root(request: Request):
    # 1. Check Request
    try:
        params = await request.json()  # json to dictionary type
        params = params['user_id']
    except:
        raise HTTPException(status_code=400, detail="Bad Request")
    
    # 2. Execute Bussiness Logic
    response = await user_service.output_user(params)

    # 3. Response
    return response

# delete user
@router.delete("/kingdom/user")
async def user_root(request: Request):
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
