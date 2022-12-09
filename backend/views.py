from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from . import forms


def signup_view(request):
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = forms.SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


def home_view(request):
  if request.user.is_authenticated:
    return redirect('app')
  return render(request, 'home.html')


@login_required
def app_view(request):
  return render(request, 'app.html')
