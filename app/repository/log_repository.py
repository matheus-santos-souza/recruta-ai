from motor.motor_asyncio import AsyncIOMotorDatabase
from models.log import Log

async def save_log(db: AsyncIOMotorDatabase, log: Log):
    await db.logs.insert_one(log.model_dump())
