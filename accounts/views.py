from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpUserForm
from django.contrib import messages
# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignUpUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, email=user.email, password=raw_password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.error("Sorry but , I Can't creating account for you")
    else:
        form = SignUpUserForm()

    return render(request, "registration/signup.html", {'form':form})