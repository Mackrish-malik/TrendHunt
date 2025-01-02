from django.http import JsonResponse
from .utils.mongo_connection import get_mongo_client

def test_mongo_connection(request):
    """
    Test MongoDB connection and fetch data from the specified collection.
    """
    try:
        # Get the MongoDB client and access the database
        db = get_mongo_client()

        # Access the collection (replace with your collection name)
        collection = db['test_collection']

        # Insert a test document (optional)
        collection.insert_one({"message": "Testing MongoDB connection!"})

        # Fetch all documents in the collection
        documents = list(collection.find({}, {"_id": 0}))  # Exclude the `_id` field

        # Return the documents if available
        if documents:
            return JsonResponse({'status': 'success', 'data': documents})
        else:
            return JsonResponse({'status': 'success', 'message': 'No data found in the collection.'})

    except Exception as e:
        # Handle any errors during the connection or operation
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)


# backend/app/views.py
from django.http import JsonResponse
from .utils.mongo_connection import get_mongo_client

def test_mongo(request):
    """
    Alternative endpoint to test MongoDB connection.
    """
    try:
        # Get MongoDB database
        db = get_mongo_client()

        # Access collection (replace with your collection name)
        collection = db['test_collection']  # Replace with actual collection name

        # Insert a test document (optional)
        collection.insert_one({"message": "Hello, MongoDB!"})

        # Fetch all documents in the collection
        documents = list(collection.find({}, {"_id": 0}))  # Exclude `_id` field
        return JsonResponse({"status": "success", "data": documents})
    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)})
