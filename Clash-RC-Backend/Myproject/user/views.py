from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages 
from django.contrib.auth.models import User 
from django.contrib.auth  import authenticate,  login, logout
from django.contrib.auth import login as auth_login
import re
# Create your views here.
def home(request):
    return render(request,'user/home.html')

def login(request):
    return render(request,'user/login.html')

def task(request):
    return render(request,'user/task.html')

# def task1(request):
#     return render(request,'user/task1.html')

def handleSignUp(request):
    if request.method=="POST":
        email=request.POST['email']
        username=request.POST['username']
        pass1=request.POST['Password']
        
        myuser = User.objects.create_user(username, email, pass1)
        myuser.save()
        messages.success(request, "You loged in succesfully")
        return redirect('home')

    else:
        return HttpResponse("404 - Not found")

def handeLogin(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            auth_login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("home")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("home")

    return HttpResponse("404- Not found")
   

    return HttpResponse("login")

def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('home')

def task1(request):
    if request.method=="POST":
        string=request.POST.get('text')
        s = [int(s) for s in re.findall(r'-?\d+\.?\d*', string)]
        params = {'analazed': s}
        return render(request,'user/task1.html',params)
    else:
        return HttpResponse("Error")

def task2(request):
    if request.method=="POST":
        string1=request.POST.get('text')
        date = [int(s) for s in re.findall(r'^(?P<date>\d{4}-\d{2}-\d{2})/$', string1)]
        params = {'analazed': date}
        return render(request,'user/task2.html',params)

    else:
        return HttpResponse("Error")

def task3(request):
    if request.method=="POST":
        string2=request.POST.get('text')
        str = [int(s) for s in re.findall(r"'([^']*)'", string2)]
        params = {'analazed': str}
        return render(request,'user/task3.html',params)

    else:
        return HttpResponse("Error")

def task4(request):
    if request.method=="POST":
        string3=request.POST.get('text')
        if len(string3) > 6:
            if re.match('\b[\w\.-]+@[\w\.-]+\.\w{2,4}\b', string3) != None:
                params = {'analazed': 1}
                return render(request,'user/task4.html',params)
        params = {'analazed': 0}
        return render(request,'user/task4.html',params)

    else:
        return HttpResponse("Error")

def task7(request):
    if request.method=="POST":
        string7=request.POST.get('text')
        str7 = re.sub(r'(?<!^)(?=[A-Z])', '_', string7).lower()
        params = {'analazed': str7}
        return render(request,'user/task7.html',params)

    else:
        return HttpResponse("Error")