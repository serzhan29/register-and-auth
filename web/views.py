from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.generic import View, ListView
from django.contrib.auth.forms import PasswordChangeForm
from .forms import RegistrationForm


class UserDetailView(View):
    def get(self, request, slug):
        user = User.objects.get(url=slug)
        all_users = User.objects.all()  # Получение всех пользователей
        return render(request, 'web/main.html', {"user": user,
                                                  "all_users": all_users})  # Передача всех пользователей в контекст



def index(request):
    return render(request, 'web/index.html')


def profile(request):
    return render(request, 'web/profile.html')


def user_logout(request):
    logout(request)
    return redirect('login')


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Обновляем сессию пользователя
            messages.success(request, 'Пароль успешно изменен!')
            return redirect('web:index')  # Предполагается, что у вас есть URL-адрес с именем 'user_info'
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'web/registration/change_password.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']

            if password1 == password2:
                # Создайте нового пользователя
                user = User.objects.create_user(username=username, password=password1)
                login(request, user)
                # Добавьте дополнительные поля, если необходимо
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
