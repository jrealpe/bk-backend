from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView

def index(request):
    return render(request, 'base/index.html');

class SignOutView(LogoutView):
    pass
