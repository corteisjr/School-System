from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from matricula.models.Alunos import *
from matricula.forms import AlunoForm

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

@login_required
def new_student(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        print(form.errors)
        if form.is_valid():
            boletim = form.save(commit=False)
            boletim.save()
            messages.info(request, 'Aluno cadastrado com sucesso')
            return redirect('student-list')
        else:
            messages.info(request, 'Erro encontrado, tente novamente!')
            return render(request, template_name='alunos/add-alunos.html')
            
    else:
        form = AlunoForm()
        context = {
            'form': form
        }
        return render(request, template_name='alunos/add-alunos.html', context=context)

