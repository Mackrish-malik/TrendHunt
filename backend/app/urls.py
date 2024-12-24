from django.urls import path
from .views import test_mongo_connection

urlpatterns = [
    path('test-mongo/', test_mongo_connection, name='test-mongo'),
]
