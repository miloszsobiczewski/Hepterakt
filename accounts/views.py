from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm


def logout_view(request):
    logout(request)
    return redirect('/accounts/login/')


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('/payments/')
    else:
        form = AuthenticationForm()
    return render(request, "accounts/login.html", {'form': form})
