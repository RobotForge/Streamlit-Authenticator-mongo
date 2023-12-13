from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi



# Connect to the MongoDB database

try:
    uri = "mongodb connection string"
    # Create a new client and connect to the server
    client = MongoClient(uri)
    db = client["db"]
    collection = db["collection"]
except Exception as e:
    print(e)
