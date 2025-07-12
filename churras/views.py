import json
from django.shortcuts import render, get_object_or_404
from .models import Prato

# Create your views here.
def index(request):
    #lista_pratos = Prato.objects.all()
    lista_pratos = Prato.objects.order_by('-date_prato').filter(publicado=True)
    return render(request, 'index.html', {'lista_pratos': lista_pratos})

def churrasco(request, id):
    prato = get_object_or_404(Prato, id=id)
    return render(request, 'churrasco.html', {'prato': prato})

def buscar(request):
    nome_a_buscar = request.GET.get('buscar', '').strip()
    lista_pratos = Prato.objects.none()#Inicia o queryset vazio
    if nome_a_buscar:
       lista_pratos = Prato.objects.order_by('-date_prato').filter(publicado=True, nome_prato__icontains=nome_a_buscar) 
    return render(request, 'index.html', {'lista_pratos': lista_pratos})
