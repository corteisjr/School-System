from django.urls import path
from matricula.views.matriculaView import *

urlpatterns = [ 
    path("boletim-list", boletim_list, name='boletim-list'),
    path("boletim/<int:id>", see_student, name='boletim'),
    path("newBoletim", new_student, name='new-student'),
    path('update/<int:id>', update_boletim, name='update-boletim'),
    path('delete/<int:id>', DeleteBoletim, name='delete-boletim')
]
