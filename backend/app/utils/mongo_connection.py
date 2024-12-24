from pymongo import MongoClient

def get_mongo_collection():
    try:
        # Connect to MongoDB
        client = MongoClient('mongodb://localhost:27017/')  # Replace with your MongoDB URI if different
        db = client['trendhunt_db']  # Database name
        collection = db['instagram_posts']  # Collection name
        return collection
    except Exception as e:
        raise Exception(f"MongoDB Connection Error: {str(e)}")
