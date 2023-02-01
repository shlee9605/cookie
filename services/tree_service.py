from models.users import Users
from structures import building_structure,product_structure

async def edit_building(id, params):
    params = Users(
        user_id=id,
        buildings=params
    )
    result = await building_structure.edit(params)
    return result

async def edit_product(id, params):
    params = Users(
        user_id=id,
        products=params
    )
    result = await product_structure.edit(params)
    return result
