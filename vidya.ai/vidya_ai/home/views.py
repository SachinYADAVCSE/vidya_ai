from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login

# Create your views here.
def index(request):
    return render(request, 'home/index.html')

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate( username=username, password=password)

        if user is not None:
            login()
            messages.success(request, 'You have been Loged In')
            redirect(request, 'home:index')

    return render(request, 'home/login.html')

def register(request):
    form = CreateUserForm()
    #it is kind of Map used to pass data
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account is Created for ' + user)
            return redirect('home:login')

    context = {'form': form}
    return render(request, 'home/register.html', context)