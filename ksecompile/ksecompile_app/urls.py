from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('login/', login_page, name='login'),
    path('logout/', logout_page, name='logout'),
    path('register/', register_page, name='register'),
]