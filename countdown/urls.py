from django.urls import path
from . import views

urlpatterns = [
    path('counter/', views.counter_view, name='counter'),  # Ensure this URL pattern ends with a slash
    path('admin_counter/', views.admin_counter_view, name='admin_counter'),
    path('login/', views.counter_view, name='login'),  # Use counter_view for login
    path('logout/', views.counter_view, name='logout'),  # Use counter_view for logout
]
