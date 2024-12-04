import motor.motor_asyncio
from config import MONGO_URL, DATABASE_NAME
# MongoDB setup
#MONGO_URL = "mongodb://localhost:27017"  # Replace with your MongoDB connection string
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URL)
db = client[DATABASE_NAME]  # Specify your database name
collection = db['database']  # Specify your collection name

class Database:
    def __init__(self, id, up_name):
        self.id = str(id)
        self.up_name = up_name

async def update_as_name(id, mode):
    result = await collection.find_one({"id": str(id)})
    if not result:
        data = {
            "id": str(id),
            "up_name": False
        }
        await collection.insert_one(data)
    else:
        await collection.update_one({"id": str(id)}, {"$set": {"up_name": mode}})

async def get_data(id):
    result = await collection.find_one({"id": str(id)})
    if not result:
        new_user = {
            "id": str(id),
            "up_name": False
        }
        await collection.insert_one(new_user)
        result = await collection.find_one({"id": str(id)})
    return result

async def full_userbase():
    users = await collection.find().to_list(None)
    return users

async def query_msg():
    query = collection.find({}, {"id": 1}).sort("id")
    result = await query.to_list(None)
    return result
