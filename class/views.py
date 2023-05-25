from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
import json
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as user_login
from django.contrib.auth import logout as user_logout
# Create your views here.



def login(request):
    userCode = json.loads(request.body)
    userCode = userCode['userCode']['userCode']

    if userCode == '1234':
        print(userCode)
        return redirect('classroom')

    


def homepage(request):
    #return HttpResponse('welcome to vClass')
    context = {}
    user  = None
    form = loginform(request.POST)
    welcome = 'Welcome to virtual classroom'
    if request.method == 'POST':
        if form.is_valid():
            #action here
            #form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            #authenticate and log user in at backend
            user = authenticate(username=username, password=password)
            #print(request.user)
            if user is not None:
                user_login(request, user)
                print(request.user)                
                return redirect ('xltutorial')
                
            else:
                messages.info(request, 'Username or Password is incorrect')
                return render (request, 'homepage.html', {'form':form})
    else:
        form = loginform()
        user_logout(request)
        print(request.user)
    return render (request, 'homepage.html', {'form':form}) 







def xltutorial(request):
    n = 'lesson_studies'
    context = {'n':n}
    return render (request, 'xlhomepage.html', context)



def classroom(request):
    #return HttpResponse('You are in the CLASSROOM')
    n ='lesson_studies'
    numb = [i for i in range(1,100,1)]
    welcome = 'Welcome to virtual classroom'
    context = {'numb':numb,  'n':n}
    return render (request, 'classroom.html', context)


def guestroom(request):
    return render (request, 'inside.html')







def register(request):
    form = UserCreationForm(request.POST)
    context = {}
    
    if request.method == 'POST':
        if form.is_valid():
            #action here
            #form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password2']

            #authenticate and log user in at backend
            user = authenticate(username=username, password=password)
            #print(request.user)
            if user is not None:
                user_login(request, user)
                #print(request.user)
                context = {'msg': 'Login details created sucessfuly!'}
                return render (request, 'confirmation.html', context)
                
            else:
                context = {'msg': 'Sorry! could not create login details, Try again'}
                messages.info(request, 'Username or Password is incorrect')
                return render (request, 'useraccount.html', {'form':form}, context)
            
        pass
        #print(form.errors.as_data)           
    else:
        form = UserCreationForm()
    return render (request, 'useraccount.html', {'form':form}) 