from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

# Create your views here.
def signup (request):
    form = UserCreationForm(request.POST or None)

    if form.is_valid():
        form.save()
        password = form.cleaned_data.get('password1')
        username = form.cleaned_data.get('username')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('home')

    return render(request, 'accounts/signup.html', {'form':form})
