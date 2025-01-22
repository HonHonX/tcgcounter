from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.counter_view, name='counter'),  # Ensure this URL pattern ends with a slash
    path('admin_counter/', views.admin_counter_view, name='admin_counter'),
    path('login/', auth_views.LoginView.as_view(template_name='countdown/counter.html', redirect_authenticated_user=True), name='login'),  # Use Django's login view
    path('logout/', auth_views.LogoutView.as_view(next_page='/counter/'), name='logout'),  # Use Django's logout view
]
