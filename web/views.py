from django.shortcuts import render


def index(request):
    return render(request, 'web/index.html')


def profile_view(request):
    return render(request, 'web/profile.html')