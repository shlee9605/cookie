from models import mongodb
from models.users import Users

async def input(params):
    return await mongodb.engine.save(params)

async def output(params):
    return await mongodb.engine.find(Users, Users.user_id==params)

async def extract(params):
    return await mongodb.engine.remove(Users, Users.user_id==params)