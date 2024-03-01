from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import os

username = os.environ.get("CHAIN_MAKER_DB_ROOT_USERNAME")
password = os.environ.get("CHAIN_MAKER_DB_ROOT_PASSWORD")
db_name = os.environ.get("CHAIN_MAKER_DB_NAME")
host = "db"
port = "27017"

try:
    # Create a MongoClient to the running MongoDB instance
    client = MongoClient(f"mongodb://${username}:${password}@{host}:${port}/")

    # Select the database
    db = client[db_name]  # replace 'database_name' with your database name

    # Select the collection
    collection = db["Attacks"]  # replace 'collection_name' with your collection name

    # Fetch all documents from the collection
    documents = collection.find()

    # Print all documents
    for document in documents:
        print(document)

except ConnectionFailure as e:
    print(f"MongoDB connection error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
