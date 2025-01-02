from django.urls import path
from .views import test_mongo_connection
from django.urls import path
from .views import test_mongo

urlpatterns = [
    path('test-mongo/', test_mongo_connection, name='test-mongo'),
    path('test-mongo/', test_mongo, name='test-mongo'),
]
