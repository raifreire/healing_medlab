from django.shortcuts import render
from medico.models import DadosMedico,DatasAbertas

def home(request):
    if request.method == "GET":
        medicos = DadosMedico.objects.all()
        return render(request, 'home.html',{'medicos':medicos})
