from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import SignupForm
from .models import Profile

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            # Create User
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                password=form.cleaned_data['password']
            )
            # Create Profile
            profile = form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('login_view')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            if user.profile.user_type == 'Patient':
                return redirect('patient_dashboard')
            else:
                return redirect('doctor_dashboard')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')
def home_view(request):
    return render(request, 'home.html')


@login_required
def patient_dashboard(request):
    if request.user.profile.user_type == 'Patient':
        return render(request, 'patient_dashboard.html')
    return redirect('login_view')


@login_required
def doctor_dashboard(request):
    if request.user.profile.user_type == 'Doctor':
        return render(request, 'doctor_dashboard.html')
    return redirect('login_view')


def logout_view(request):
    logout(request)
    return redirect('login_view')
