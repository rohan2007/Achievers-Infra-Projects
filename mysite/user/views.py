from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    return render(request, 'user/index.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        user = User.objects.create_user(username=username, email=email, password = password, first_name = firstname, last_name = lastname)
        user.save()
        return HttpResponse('User created')
    elif request.method == 'GET':
        return render(request, template_name = 'user/index.html')