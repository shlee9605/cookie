from models import mongodb
from models.users import Users

# Input An User
async def input(params):
    return await mongodb.engine.save(params)

# Output An User
async def output(params):
    return await mongodb.engine.find_one(Users, Users.user_id==params)

# Erase An User
async def erase(params):
    return await mongodb.engine.remove(Users, Users.user_id==params)