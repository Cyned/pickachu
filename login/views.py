from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from . import forms


class Login(View):

    form_class = forms.UserFormLog
    template_name = 'login/login.html'

    def get(self, request):
        form = self.form_class(None)

        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        username = form['username'].value()
        password = form['password'].value()

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home:home')
        return redirect('login:login')


class LogUp(View):

    form_class = forms.UserFormRegistration
    template_name = 'login/log_up.html'

    def get(self, request):
        form = self.form_class(None)

        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            password = form.cleaned_data['password']

            user.set_password(password)
            user.save()

            login(request, user)
            return redirect('home:home')
        return redirect('login:log_up')


class LogOut(View):

    @method_decorator(login_required)
    def get(self, request):
        logout(request)
        return redirect('home:home')
