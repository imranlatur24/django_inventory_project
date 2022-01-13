from django.shortcuts import render,redirect
from .forms import CreateUserForm,UserUpdateForm,ProfileUpdateForm #add email to registration page
# Create your views here.
from django.views.decorators.csrf import csrf_protect
#add flash messages
from django.contrib import messages

@csrf_protect
def register(request):
    if request.method=='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'{username} account has been created successfully please log in')
            return redirect('dashboard-index')
    else:
        form=CreateUserForm()
    context={
        'form':form
    }
    return render(request,'user/register.html',context)

#get user data 
def profilefun(request):
    return render(request,'user/profile.html')

#update user data 
@csrf_protect
def profile_update(request): #for update
    if request.method=='POST':
        user_form=UserUpdateForm(request.POST,instance=request.user)
        profile_form=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profilemodel)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')

    else:#for get 
        user_form=UserUpdateForm(instance=request.user)
        profile_form=ProfileUpdateForm(instance=request.user.profilemodel)

    context={
        'user_form':user_form,
        'profile_form':profile_form,
    }
    return render(request,'user/profile_update.html',context)
