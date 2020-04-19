from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)    
        if form.is_valid():  # must be valid according to django
            form.save()  # save user information
            print('hit valid')
            username = form.cleaned_data.get('username')
            messages.success(request, "Your accound has been created! You are now able to log in.")
            return redirect('login')  # name for url pattern to login page
        
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')