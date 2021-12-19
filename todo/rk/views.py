from django.shortcuts import render
from .models import Computer, Program

def GetComputer(request, id):
    return render(request, 'main/computer.html', {'data' : {
        'computer': Computer.objects.filter(id=id)[0],
        'programs': Program.objects.filter(computer_id=id),
        'computers': Computer.objects.all(),
    }})

def index(request):
    return render(request, 'main/index.html', {'data' : {
        'computers': Computer.objects.all()
    }})
