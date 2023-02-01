from structures import user_structure



async def input_user(params):
    result = await user_structure.input(params)
    return result

async def output_user(params):
    result = await user_structure.output(params)
    return result

async def extract_user(params):
    result = await user_structure.extract(params)
    return result