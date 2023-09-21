from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.models import User

from .forms import RegistrationForm


def index(request):
    return render(request, 'web/index.html')


def profile(request):
    return render(request, 'web/profile.html')


def user_logout(request):
    logout(request)
    return redirect('login')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            surname = form.cleaned_data['surname']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']

            if password1 == password2:
                # Создайте нового пользователя
                user = User.objects.create_user(username=username, password=password1)
                login(request, user)
                # Добавьте дополнительные поля, если необходимо
                user.last_name = surname
                user.save()
                messages.success(request, 'Вы успешно зарегистрированы.')
                return redirect('accounts/profile')
            else:
                messages.error(request, 'Пароли не совпадают.')
        else:
            messages.error(request, 'Ошибка в форме.')
    else:
        form = RegistrationForm()
    return render(request, 'web/registration/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('web:profile')
    else:
        form = AuthenticationForm()
    return render(request, 'web/registration/login.html', {'form': form})
