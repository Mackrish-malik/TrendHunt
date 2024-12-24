from django.http import JsonResponse
from .utils.mongo_connection import get_mongo_collection

def test_mongo_connection(request):
    try:
        collection = get_mongo_collection()
        test_data = collection.find_one()  # Fetch one document
        if test_data:
            return JsonResponse({'message': 'MongoDB Connected!', 'data': test_data})
        return JsonResponse({'message': 'MongoDB Connected! No data found.'})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
