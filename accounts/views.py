from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
from contacts.models import Contact

# Create your views here.

def register(request):
    if request.method == 'POST':
        # Get formfield values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Password validation
        if password == password2:
            # Email validation
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already taken')
                return redirect('register')
            else: 
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email already taken')
                    return redirect('register')
                else:
                    # Passes username and email validation: Username and Email are avaiable for registration.
                    user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)   
                    user.save()
                    messages.success(request, 'You are now registered. Please log in. ')
                    return redirect('login')                
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        #Login the user
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in.')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')

        return redirect('login')
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('index')

def dashboard(request):
    inquiries = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
    
    context = {
        'inquiries': inquiries,
    }

    return render(request, 'accounts/dashboard.html', context)