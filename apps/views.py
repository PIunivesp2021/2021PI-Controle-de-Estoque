from django.shortcuts import render, redirect
from app.forms import ControleForm
from app.models import Controle


# Create your views here.

def home(request):
    data = {}
    search = request.GET.get('search')
    if search:
        data['db'] = Controle.objects.filter(Empenho__icontains=search)
    else:
        data['db'] = Controle.objects.all()
    return render(request, 'index.html', data)


def form(request):
    data = {}
    data['form'] = ControleForm()
    return render(request, 'form.html', data)


def create(request):
    form = ControleForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')


def view(request, pk):
    data = {}
    data['db'] = Controle.objects.get(pk=pk)
    return render(request, 'view.html', data)


def edit(request, pk):
    data = {}
    data['db'] = Controle.objects.get(pk=pk)
    data['form'] = ControleForm(instance=data['db'])
    return render(request, 'form.html', data)


def update(request, pk):
    data = {}
    data['db'] = Controle.objects.get(pk=pk)
    form = ControleForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')

def delete(request, pk):
    db = Controle.objects.get(pk=pk)
    db.delete()
    return redirect('home')
