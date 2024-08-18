# Create your views here.
from email import message
from genericpath import exists
from django import conf, views
from django.views import View
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.core.mail import EmailMessage
from django.contrib.auth.decorators import login_required


# Create your views here.

def register(request):
    if request.method == 'POST':
        username =  request.POST['username']
        email = request.POST['email']
        first_name =  request.POST['first_name']
        last_name =  request.POST['last_name']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if password == confirm_password:   
            if User.objects.filter(username  = username).exists():
                print('Oops! Student name already exist!')
                messages.warning(request, 'Oops! Student Data already exist')
                return redirect('register')
            elif User.objects.filter(email = email).exists():
                print('Oops! Email has been used')
                messages.warning(request, 'Oops! Student Data already exist')
                return redirect('register')
            elif User.objects.filter(last_name = last_name).exists():
                print('Oops! Student Data already exist')
                messages.warning(request, 'Oops! Student Data already exist')
                return redirect ('register')
            else:
                user = User.objects.create_user(username = username, first_name = first_name, last_name = last_name, email = email, password = password)
                user.set_password(password)
                user.save()               
                print ('User account created')
                messages.success(request, 'Account created successfully, Login',)
                return render(request, 'authentication/login.html')
        elif len(password) < 6:
            print('password too short')
            messages.error(request, 'Password too short, It should be 6 or more characters')
            return redirect('register')
        else:
            print("password doesn't match")
            messages.error(request, "Password doesn't match, Try again")
            return redirect('register')
    else:
        return render(request, 'authentication/register.html')
            
            
# @login_required    
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = User.objects.get(last_name = username), password = password)
        # user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request, user)
            print(f"Welcome to the student attendance dashboard {user}")
            messages.success(request, f"Welcome to Your Attendance Dashboard {user}")
            return redirect('attendance')
        else:
            print('Your email or password is incorrect, Please fill all fields correctly')
            messages.warning(request, 'Oops! Invalid Student Details')
            return redirect('login')
    else:
        return render(request, 'authentication/login.html')
    
    

def logout(request):
    auth.logout(request)
    print("You have been logged out")
    messages.success(request, "You have been logged out")
    return redirect('login')
       
 