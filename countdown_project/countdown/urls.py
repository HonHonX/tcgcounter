from django.urls import path
from . import views

urlpatterns = [
    path('/counter', views.counter_view, name='counter'),
    path('admin_counter/', views.admin_counter_view, name='admin_counter'),
]
