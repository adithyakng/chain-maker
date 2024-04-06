from pymongo.mongo_client import MongoClient
from pymongo.errors import ConnectionFailure
from helpers.loadJSON import create_attack
import os

username = os.environ.get("CHAIN_MAKER_DB_ROOT_USERNAME")
password = os.environ.get("CHAIN_MAKER_DB_ROOT_PASSWORD")
db_name = os.environ.get("CHAIN_MAKER_DB_NAME")
host = "cluster0"
port = "27017"


def getAttackDB():
    try:
        # Create a MongoClient to the running MongoDB instance
        client = MongoClient("mongodb+srv://"+username+":"+password+"@cluster0.xebr2ot.mongodb.net/?retryWrites=true&w=majority")

        # Select the database
        db = client[db_name]  # replace 'database_name' with your database name

        # Select the collection
        collection = db["attackDB"]  # replace 'collection_name' with your collection name


        # Fetch all documents from the collection
        documents = collection.find()
        # json_data = {}
        # for document in documents:
        #     json_data.append(document)

       

        return {'success' : True, 'attacks' : create_attack(documents)}

    except ConnectionFailure as e:
        print(f"MongoDB connection error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    
    return {'success': False, 'message': "Unable to connect to MongoDB"}