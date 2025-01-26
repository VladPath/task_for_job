from django.shortcuts import render
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.

def login(request):
    return render(request, 'my_app/login.html', context={})


def patients(request):
    return render(request,'my_app/patients.html', context={})
    
    