from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request, 'my_app/login.html', context={})


def patients(request):
    return render(request,'my_app/patients.html', context={})
    
    