# your_app/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')  # Render a home.html template

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the new user to the database
            login(request, user)  # Automatically log in the user after signup
            return redirect('home')  # Redirect to a homepage or another view
    else:
        form = UserCreationForm()  # Display an empty form
    return render(request, 'signup.html', {'form': form})
