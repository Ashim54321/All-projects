from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect,HttpResponse


def index(request):
    
   return render(request, 'index.html')



def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            print("123")
            form.save()
            return redirect('index.html')
    else:
        form = UserCreationForm()
    return render(request, 'sign.html', {'form': form})

def login(request):
    if request.user.is_authenticated:
        return redirect("index")

    if request.method == 'POST':
        user = authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            return redirect('index')
        
        else:
            form = UserCreationForm()
        return render(request, 'login.html', {'form': form})
    return render(request,"login.html")
    