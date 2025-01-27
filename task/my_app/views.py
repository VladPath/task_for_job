from django.shortcuts import render
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.decorators import login_required

# Create your views here.

def login(request):
    return render(request, 'my_app/login.html', context={})


@login_required
def patients(request):
    return render(request,'my_app/patients.html', context={})
    
    