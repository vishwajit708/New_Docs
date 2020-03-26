from django.shortcuts import render
from .forms import UserRegistrationForm,UserEditForm,ProfileEditForm
from django.views import View
from .models import Profile
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.


class RegistrationView(View):
    def get(self,request):
        user_form=UserRegistrationForm()
        return render(request,'registration/register.html',{"user_form":user_form})
    def post(self,request):
        user_form=UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user=user_form.save(commit=False)
            new_user.username=user_form.cleaned_data['email']
            new_user.set_password(user_form.cleaned_data.get('password'))
            new_user.save()
            Profile.objects.create(user=new_user)
            return render(request,'registration/register_done.html')

@login_required
def edit(request):
    user_form = UserEditForm(instance=request.user)
    profile_form = ProfileEditForm(instance=request.user.profile)
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile,data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated successfully')

    return render(request,"edit.html",{'user_form': user_form,'profile_form': profile_form})
