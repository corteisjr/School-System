from django.urls import path
from matricula.views.alunosView import *

urlpatterns = [
    path("student-list/", studentes_list, name='student-list'),
    path("aluno/<int:id>", see_student, name='see-student'),
    path("create/", new_student, name='create-student'), 
    path('delete/<int:id>', DeleteAluno, name='delete-aluno')
]
