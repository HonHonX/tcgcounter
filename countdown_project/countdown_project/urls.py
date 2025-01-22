from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('counter', include('countdown.urls')),  # Include the countdown app URLs
    path('', include('countdown.urls')),  # Include the countdown app URLs for the home page
]
