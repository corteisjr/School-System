from django.urls import path
from matricula.views.homeView import home_view

urlpatterns = [
    path("", home_view, name='home_view')
]
