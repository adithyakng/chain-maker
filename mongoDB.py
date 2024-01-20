from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

try:
    # Create a MongoClient to the running MongoDB instance
    client = MongoClient('mongodb://localhost:27017/')
    
    # Select the database
    db = client['Chain_Reaction']  # replace 'database_name' with your database name
    
    # Select the collection
    collection = db['Attacks']  # replace 'collection_name' with your collection name
    
    # Fetch all documents from the collection
    documents = collection.find()
    
    # Print all documents
    for document in documents:
        print(document)

except ConnectionFailure as e:
    print(f"MongoDB connection error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
