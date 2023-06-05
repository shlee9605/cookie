from models import mongodb
from libs.scheduleUtil import scheduler

async def on_app_start():
    await mongodb.connect()
    await scheduler.start()

async def on_app_shutdown():
    mongodb.close()
    scheduler.stop()
