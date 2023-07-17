from django.shortcuts import render, get_object_or_404, redirect
from .forms import CidadeForm
from .models import Cidade

# Create your views here.

def cidade_editar(request,id):
    cidade = get_object_or_404(Cidade,id=id)
   
    if request.method == 'POST':
        form = CidadeForm(request.POST,instance=cidade)

        if form.is_valid():
            form.save()
            return redirect('cidade_listar')
    else:
        form = CidadeForm(instance=cidade)

    return render(request,'cidades/form.html',{'form':form})


def cidade_remover(request, id):
    cidade = get_object_or_404(Cidade, id=id)
    cidade.delete()
    return redirect('cidade_listar') 


def cidade_criar(request):
    if request.method == 'POST':
        form = CidadeForm(request.POST)
        if form.is_valid():
            form.save()
            form = CidadeForm()
            return redirect('cidade_listar')
    else:
        form = CidadeForm()

    return render(request, "cidades/form.html", {'form': form})


def cidade_listar(request):
    cidades = Cidade.objects.all()
    context ={
        'cidades': cidades
    }
    return render(request, "cidades/cidades.html", context)