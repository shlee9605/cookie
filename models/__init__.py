import os
from motor.motor_asyncio import AsyncIOMotorClient
from odmantic import AIOEngine

from models.users import Users

# db config
class MongoDB:
    def __init__(self):
        self.client = None
        self.engine = None
    
    async def connect(self):
        self.client = AsyncIOMotorClient(os.environ["MONGO_URL"])
        self.engine = AIOEngine(client=self.client, database=os.environ["MONGO_DATABASE"])
        await self.engine.configure_database([Users])   # for Index, Unique etc..
        print('DB와 성공적으로 연결이 되었습니다.')
    
    def close(self):
        self.client.close()

mongodb = MongoDB()