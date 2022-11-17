from django.urls import path
from matricula.views.alunosView import *

urlpatterns = [
    path("student-list/", studentes_list, name='student-list'),
    path("create/", new_student, name='create-student'),
]
