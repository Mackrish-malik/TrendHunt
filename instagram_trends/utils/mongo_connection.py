# utils/mongo_connection.py
from pymongo import MongoClient

def get_mongo_client():
    """Establish a connection to the MongoDB instance."""
    try:
        # Replace 'localhost' with your MongoDB URI if hosted remotely
        client = MongoClient('mongodb://localhost:27017/')  # Default local MongoDB URI
        print("MongoDB connected successfully.")
        return client
    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")
        return None
