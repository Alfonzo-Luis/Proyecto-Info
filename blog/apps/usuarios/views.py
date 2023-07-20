from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.generic import CreateView
from .forms import RegistroForm
from django.urls import reverse_lazy

# Create your views here.

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home') #redireccion a la pag de home post login
        else:
            messages.error(request, 'usuario o contraseña invalido, intente de nuevo')
    
    return render(request, 'usuarios/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')

# registro de usuarios
class Registro(CreateView):
    # formulario de django
    form_class = RegistroForm
    success_url = reverse_lazy('login')
    template_name = 'usuarios/registro.html'