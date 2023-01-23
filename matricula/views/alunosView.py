from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from matricula.models.Alunos import *
from matricula.forms import AlunoForm


@login_required
def studentes_list(request):
    students_list = Aluno.objects.all().order_by("created_at")
    paginator = Paginator(students_list, 6)
    page = request.GET.get("page")
    alunos = paginator.get_page(page)
    context = {"alunos": alunos}
    return render(request, template_name="alunos/alunos.html", context=context)


@login_required
def see_student(request, id):
    students = Aluno.objects.filter(id=id)
    context = {"students": students}
    return render(request, template_name="alunos/detalhes.html", context=context)


@login_required
def new_student(request):
    if request.method == "POST":
        form = AlunoForm(request.POST)
        print(form.errors)
        if form.is_valid():
            boletim = form.save(commit=False)
            boletim.save()
            messages.info(request, "Aluno cadastrado com sucesso")
            return redirect("student-list")
        else:
            messages.info(request, "Erro encontrado, tente novamente!")
            return render(request, "alunos/add-alunos.html")

    else:
        form = AlunoForm()
        context = {"form": form}
        return render(request, "alunos/add-alunos.html", context=context)


@login_required
def DeleteAluno(request, id):
    form = AlunoForm(request.POST)
    aluno = get_object_or_404(Aluno, pk=id)
    aluno.delete()
    messages.info(request, "Aluno deletado com sucesso!")
    return render(request, "alunos/alunos.html", {"form": form})
