from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)    
        if form.is_valid():  # must be valid according to django
            form.save()  # save user information
            print('hit valid')
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account created for {username}!")
            return redirect('blog-home')  # name for url pattern to blog homepage
        
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
