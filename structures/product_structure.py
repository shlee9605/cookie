from fastapi import HTTPException
from models import mongodb
from models.users import Users

async def edit(params):
    # 1. Find User
    result = await mongodb.engine.find_one(Users, Users.user_id==params['user_id'], Users.deletedAt == None)
    if not result:
        raise HTTPException(status_code=500, detail="No Matched User Found")

    # 2. Input Products
    try:
        result.products = params['products']
        await mongodb.engine.save(result)
    except:
        raise HTTPException(status_code=500, detail="Editting Products Info Failed")

    # 3. Return at Success
    return result
