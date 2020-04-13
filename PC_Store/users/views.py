from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from .forms import UserProfileForm
from .forms import UserUpdateForm
from .forms import ProfileUpdateForm
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user

            profile.save()

            username = user_form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created {username}! You can now log in')
            return redirect('login')
    else:
        user_form = UserRegisterForm()
        profile_form = UserProfileForm()
    return render(request, 'users/register.html', {'user_form':user_form, 'profile_form':profile_form })

@login_required
def profile(request):
    if request.method == 'POST':
        uu_form = UserUpdateForm(request.POST, instance=request.user)
        pu_form = ProfileUpdateForm(request.POST, instance=request.user.profile)
        if uu_form.is_valid() and pu_form.is_valid():
            uu_form.save()
            pu_form.save()

            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        uu_form = UserUpdateForm(instance=request.user)
        pu_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'uu_form': uu_form,
        'pu_form': pu_form
    }
    return render(request,'users/profile.html', context)
