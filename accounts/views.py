from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.

def register(request):
    if request.method=="POST":
        first_name= request.POST['first_name']
        last_name= request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        confirmpassword = request.POST['confirmpassword']
        if password==confirmpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username taken')
                return redirect('register')
                
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email taken')
                return redirect('register')
                    
            else:
                user=User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name, email=email)
                user.save()
                print('user created')
            return redirect('login')
        else:
            messages.info(request, 'passwords not matching')
            return redirect('register')

            
        
    else:
         return render(request, 'register.html')



