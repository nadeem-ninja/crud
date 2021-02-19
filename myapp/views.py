from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages

from myapp.forms import UserForm
from myapp.models import User


@login_required
def add_show(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            form = UserForm()
    else:
        form = UserForm()
    data = User.objects.all()

    context = {'form': form, 'show': data}
    return render(request, 'myapp/addandshow.html', context)

@login_required
def delete_data(request, id):
    dt = User.objects.get(pk=id)
    dt.delete()
    return HttpResponseRedirect('/')

@login_required
def update_view(request, id):
    if request.method == "POST":
        update = User.objects.get(pk=id)
        fm = UserForm(request.POST, instance=update)
        if fm.is_valid():
            fm.save()
            return redirect('/')
    else:
        update = User.objects.get(pk=id)
        fm = UserForm(instance=update)
    context = {'form': fm}
    return render(request, 'myapp/update.html', context)


def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'User has been successfully register')
            form.save()
    else:
        form = UserCreationForm()
    return render(request, 'myapp/signup.html', {'form': form})

@login_required
def user_login(request):
    form = AuthenticationForm()
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')
    else:
        return render(request, 'myapp/login.html', {'form': form})
