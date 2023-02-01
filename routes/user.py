from fastapi import APIRouter, Request
from models.users import Users

from services import user_service

router = APIRouter()

# add user
@router.post("/kingdom/user")
async def user_root(request: Users):
    params = Users(
        user_id=request.user_id
    )

    response = await user_service.input_user(params)
    return response

# get user info
@router.get("/kingdom/user")
async def user_root(request: Request):
    params = await request.json() # json to dictionary type
    params = params['user_id']

    response = await user_service.output_user(params)
    return response

# delete user
@router.delete("/kingdom/user")
async def user_root(request: Request):
    params = await request.json() # json to dictionary type
    params = params['user_id']

    response = await user_service.extract_user(params)
    return response