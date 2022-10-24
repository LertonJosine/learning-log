
from django.urls import path, include
from django.contrib.auth.views import LoginView
from .views import my_logout_view
from learning_logs.views import home, topics
from .views import registrar, my_login_view
urlpatterns = [
    path('login/', my_login_view, name='login' ), 
    path('logout/', my_logout_view, name='logout'),
    path('', home , name='home'),
    path('register/', registrar, name='registrar'),
    path('topics/', topics, name='topics'),
]
