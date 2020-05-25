from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
app_name = 'accounts'
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html',
                                                redirect_field_name='productos:index'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='productos/index.html'), name="logout"),
    path('registration/', views.SignUp.as_view(), name='registration'),
]
