from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse  # Import HttpResponse for the home view

# Define a simple home page view
def home(request):
    return HttpResponse("<h1>Welcome to TrendHunt!</h1><p>Backend is working!</p>")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test-mongo/', include('app.urls')),  # MongoDB test endpoint
    path('', home, name='home'),              # Root URL view
]
