from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Home view
@login_required
def home(request):
    return render(request, 'view.html')

# Login view
def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome, {user.username}')
            return redirect('home')  # Redirect to a success page.
        else:
            messages.error(request, 'Invalid username or password')
    
    return render(request, 'registration/login.html')

# Signup view
def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return render(request, 'registration/sign_up.html')

        # Check if the email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists')
            return render(request, 'registration/sign_up.html')

        try:
            myuser = User.objects.create_user(username, email, password)
            myuser.save()
            messages.success(request, 'Account created successfully')
            return redirect('login')
        except Exception as e:
            messages.error(request, 'Error creating account: ' + str(e))
            return render(request, 'registration/sign_up.html')

    return render(request, 'registration/sign_up.html')


def reset_password(request):
    response_dic = {}
    
    try:
        usern = request.POST.get('username')
        recepient = request.POST.get('email')
        pwd = request.POST.get('password')
        
        if not usern or not recepient or not pwd:
            response_dic["errmsg"] = "All fields are required."
            return render(request, "registration/ResetPassword.html", response_dic)
        
        try:
            user = User.objects.get(username=usern)
            if user.email == recepient:
                user.set_password(pwd)
                user.save()
                response_dic["errmsg"] = "Password Reset Successfully"
            else:
                response_dic["errmsg"] = "Email does not match the username"
        except User.DoesNotExist:
            response_dic["errmsg"] = "User does not exist"
        except Exception as e:
            print(e)
            response_dic["errmsg"] = "An error occurred while resetting the password"
            
    except Exception as e:
        print(e)
        response_dic["errmsg"] = "Failed to reset password"

    return render(request, 'registration/ResetPassword.html', response_dic)


def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('login')

# Tab view
@login_required
def tab(request):
    return render(request, 'view.html')

# Base view
def base(request):
    return render(request, 'base.html')
