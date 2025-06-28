from django.shortcuts import render

# Create your views here.
def index(request):
    dados = {'lista_pratos':
        {
            '1':'Picanha',
            '2':'Costela',
            '3':'Cupim',
            '4':'Fraudinha',
            '5':'Espetinho'
        }
    }
    return render(request, 'index.html', dados)

def churrasco(request):
    return render(request, 'churrasco.html')

