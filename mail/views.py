from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'mail/landing.html')

def dashboard(request):
    return render(request, "mail/dashboard.html")

def login(request):
    return render(request, "mail/login.html")

def signup(request):
    return render(request, "mail/signup.html")

