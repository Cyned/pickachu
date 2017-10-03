from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View

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

        print('-' * 100)
        print(username)
        print(password)

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home:home')
        return redirect('login:login')


class Log_up(View):

    template_name = 'login/log_up.html'

    def get(self, request):
        context = {}

        return render(request, self.template_name, context)
