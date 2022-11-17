from django.urls import path
from .views import *

urlpatterns = [
    path('login/', login_account, name='loginaccount'),
    path('logout', logout_account, name='logout_account')
]