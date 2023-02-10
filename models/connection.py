from models import mongodb

async def on_app_start():
    await mongodb.connect()

async def on_app_shutdown():
    mongodb.close()