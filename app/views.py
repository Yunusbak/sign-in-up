from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout


def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']

        if not all([first_name, last_name, username, email, password, password2]):
            return render(request, 'register.html', context={"message1": "Barcha qatorlarni to'ldiring!"})

        if password != password2:
            return render(request, 'register.html', context={"message2": "Passwordlar bir xil emas!"})

        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', context={"message3": "Bu username bilan ro'yhatdan o'tilgan!"})

        new_user = User(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name)

        new_user.set_password(password)
        new_user.save()
        return redirect('login')


    return render(request, 'register.html')


def login_view(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request, data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', context={"message" : "Username yoki Password Xato!!!"})
    return render(request, 'login.html')

def home_view(request):
    return render(request, 'home.html')
