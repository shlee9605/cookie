from models import mongodb
from models.users import Users

async def edit(params):
    result = await mongodb.engine.find_one(Users, Users.user_id==params.user_id)
    result.products = params.products
    await mongodb.engine.save(result)
    return result
