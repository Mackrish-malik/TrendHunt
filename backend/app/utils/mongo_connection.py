from pymongo import MongoClient
from django.conf import settings

def get_mongo_client():
    """
    Returns a MongoClient object connected to the MongoDB instance.
    """
    try:
        # Fetch MongoDB connection details from settings
        mongo_uri = settings.MONGO_URI  # Defined in Django settings
        mongo_db_name = settings.MONGO_DB_NAME  # Defined in Django settings

        # Create a MongoDB client
        client = MongoClient(mongo_uri)

        # Return the database instance
        db = client[mongo_db_name]
        return db
    except Exception as e:
        raise Exception(f"Error connecting to MongoDB: {str(e)}")
