from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from contextlib import asynccontextmanager
import os

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
MONGO_DB = os.getenv("MONGO_DB", "mydb")

@asynccontextmanager
async def lifespan(app):
    client = AsyncIOMotorClient(MONGO_URI, maxPoolSize=10)
    db: AsyncIOMotorDatabase = client[MONGO_DB]
    
    app.state.db = db
    try:
        yield
    finally:
        client.close()
