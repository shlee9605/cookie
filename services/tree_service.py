from structures import building_structure, product_structure, technology_structure


async def edit_technology(params):
    result = await technology_structure.edit(params)
    return result

async def edit_building(params):
    result = await building_structure.edit(params)
    return result

async def edit_product(params):
    result = await product_structure.edit(params)
    return result
