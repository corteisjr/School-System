from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from matricula.models.Alunos import *

@login_required
def studentes_list(request):
    students_list = Aluno.objects.all()
    paginator = Paginator(students_list, 6)
    page = request.GET.get('page')
    alunos = paginator.get_page(page)
    context = {
        'alunos': alunos
    }
    return render(request, template_name='alunos/alunos.html', context=context)

