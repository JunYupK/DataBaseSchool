from ast import Pass
from msilib.schema import CustomAction
from django.shortcuts import render, redirect, HttpResponse
from .forms import SignupForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib import auth
from django.contrib.auth.decorators import login_required
# Create your views here.

def login_view(request):
  if request.method == 'POST':
    form = AuthenticationForm(request=request, data=request.POST)
    print(form.is_valid())
    print(request.POST.get('username'), request.POST.get('password'))
    if form.is_valid():
      print('12')
      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password')
      print(password)
      user = auth.authenticate(
        request=request,
        username=username,
        password=password
      )
      print('w')
      if user is not None:
        auth.login(request, user)
        return redirect('/')

    return redirect('account:login')
  
  else:
    form = AuthenticationForm()
    return render(request, 'account/login.html', {'form' : form})

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.first_name = request.POST.get('first_name')
            user.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            auth.login(request, user)
            return redirect('app:main')
    
    else:
        form = SignupForm()
    
    return render(request, 'account/signup.html', {'form' : form})    

def change_password(request):
  if request.method == 'POST':
    form = PasswordChangeForm(request.user, request.POST)
    if form.is_valid():
      print('a')
      form.save()
      return redirect('app:main')
  else:
    form = PasswordChangeForm(request.user)
  
  return render(request, 'account/mypage', {'form' : form})

@login_required(login_url='account:login')
def mypage(request):
  print(request.path)
  if request.method == 'POST':
    form = PasswordChangeForm(request.user, request.POST)
    if form.is_valid():
      user = form.save()
      return redirect('app:main')
  else:
    form = PasswordChangeForm(request.user)
  
  return render(request, 'account/mypage.html', {'form' : form})