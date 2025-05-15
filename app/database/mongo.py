from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from contextlib import asynccontextmanager
import os

MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB = os.getenv("MONGO_DB")

@asynccontextmanager
async def lifespan(app):
    client = AsyncIOMotorClient(MONGO_URI, maxPoolSize=10)
    db: AsyncIOMotorDatabase = client[MONGO_DB]

    logs_collection = db["logs"]
    await logs_collection.create_index("request_id", unique=False)
    
    app.state.db = db
    yield
    client.close()
