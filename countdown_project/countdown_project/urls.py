from django.contrib import admin
from django.urls import path
from countdown.views import counter_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('counter', counter_view, name='counter'),
    path('', counter_view, name='home'),
]
