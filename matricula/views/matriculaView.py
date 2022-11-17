from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from matricula.models.Boletim import *
from matricula.forms import BoletimForm

@login_required
def boletim_list(request):
    boletim_list = DadosPessoais.objects.all()
    paginator = Paginator(boletim_list, 6)
    page = request.GET.get('page')
    boletins = paginator.get_page(page)
    context = {
        'boletins': boletins
    }
    return render(request, template_name='matricula/matricula.html', context=context)

@login_required
def see_student(request, id):
    students = DadosPessoais.objects.filter(id=id)
    context = {
        'students': students
    }
    return render(request, template_name='matricula/boletim.html', context=context)
    

@login_required
def new_student(request):
    if request.method == 'POST':
        form = BoletimForm(request.POST)
        print(form.errors)
        if form.is_valid():
            boletim = form.save(commit=False)
            boletim.save()
            messages.info(request, 'Boletim cadastrado com sucesso')
            return redirect('boletim-list')
        else:
            messages.info(request, 'Erro encontrado, tente novamente!')
            return render(request, template_name='matricula/addBoletim.html')
            
    else:
        form = BoletimForm()
        context = {
            'form': form
        }
        return render(request, template_name='matricula/addBoletim.html', context=context)
 
@login_required
def update_boletim(request, id):
    boletim = get_object_or_404(DadosPessoais, pk=id)
    form = BoletimForm(instance=boletim)
    
    if(request.method == 'POST'):
        form = BoletimForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Boletim actualiado com sucesso')
            return redirect('boletim-list')
        else:
            return render(request, 'matricula/update-boletim.html', {'form': form, 'boletim': boletim})
    else:
        return render(request, 'matricula/update-boletim.html', {'form': form, 'boletim': boletim})
    
@login_required
def DeleteBoletim(request, id):
    form = BoletimForm(request.POST)
    boletim = get_object_or_404(DadosPessoais, pk=id)
    boletim.delete()
    messages.info(request, "Boletim deletado com sucesso!")
    return render(request, 'matricula/matricula.html', {'form': form})
    
    