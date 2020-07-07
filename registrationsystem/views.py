from django.shortcuts import render, redirect
#from django.http import HttpResponse
#from django.contrib.auth.forms import UserCreationForm
from registrationsystem.forms import(
    RegistrationForm, 
    EditProfileForm
   
) 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
#from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    #return HttpResponse('Welcome to my Registration System')
    numbers = [1,2,3,4,5]
    name = 'apoorva'

    args ={'myname':name, 'mynums':numbers}
    return render(request,'registerapp/home.html',args)


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/mypage')
    else:
        form = RegistrationForm()
        args = {'form':form}
        return render(request,'registerapp/regform.html', args)


def profile(request):
    args ={'user':request.user}
    return render(request, 'registerapp/profile.html', args)


def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance = request.user)

        if form.is_valid:
            form.save()
            return redirect('/mypage/profile')

    else:
        form = EditProfileForm(instance=request.user)
        args ={'form':form}
        return render(request, 'registerapp/edit_profile.html', args)



def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data = request.POST,user= request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/mypage/profile')
        
        else:
            return redirect('/mypage/change_password')

    else:
        form = PasswordChangeForm(user=request.user)
        args ={'form':form}
        return render(request, 'registerapp/change_password.html', args)





