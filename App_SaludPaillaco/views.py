from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, 'inicio.html')

def registrarse(request):
    return render(request, 'registrarse.html')