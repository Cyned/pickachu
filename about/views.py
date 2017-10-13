from django.shortcuts import render
from django.views.generic import View


class Main(View):
    template_name = 'about/home.html'

    def get(self, request):

        return render(request, self.template_name)
