from django.contrib import admin
from django.urls import path, include
from countdown import views  # Correct the import statement to import views from the countdown app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('counter/', include('countdown.urls')),  # Remove the trailing slash
    path('', views.home_view, name='home'),  # Add a default view for the home page
    path('csrf_failure/', views.csrf_failure, name='csrf_failure'),  # Add the CSRF failure view
]
