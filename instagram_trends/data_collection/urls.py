from django.urls import path
from . import views

urlpatterns = [
    path('fetch-instagram-data/', views.fetch_instagram_data, name='fetch_instagram_data'),
]
