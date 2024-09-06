from django.contrib import admin
from django.urls import path, include
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),    
    path('api/',include('quotes.urls')),
    path('', views.home, name='home'),  # Home view URL pattern
    # Custom signup view
    path('signup/', views.signup, name='signup'),
    # Built-in login and logout views
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
]   
