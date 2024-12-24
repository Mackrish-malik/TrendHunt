# data_collection/views.py
from django.http import JsonResponse
from utils.mongo_connection import get_mongo_client
import requests
from django.http import JsonResponse

def fetch_data_from_mongo(request):
    client = get_mongo_client()  # Get the MongoDB client
    
    if client:
        # Select your database (replace 'my_database' with your actual DB name)
        db = client['my_database']
        
        # Select your collection (replace 'posts' with your collection name)
        posts_collection = db['posts']
        
        # Fetch all documents from the collection (or any query you need)
        posts = posts_collection.find()
        
        # Convert the MongoDB cursor to a list and return it as JSON
        posts_list = list(posts)
        return JsonResponse(posts_list, safe=False)  # safe=False allows non-dictionary data
    else:
        return JsonResponse({'error': 'Could not connect to MongoDB'}, status=500)

def fetch_instagram_data(request):
    url = "https://graph.instagram.com/me/media"
    params = {
        'fields': 'id,caption,media_type,media_url,permalink',
        'access_token': 'YOUR_ACCESS_TOKEN'
    }
    response = requests.get(url, params=params)
    data = response.json()
    # Process and save data to the database
    return JsonResponse(data)
