from django.urls import path
from matricula.views.alunosView import *

urlpatterns = [
    path("student-list/", studentes_list, name='student-list'),
]
