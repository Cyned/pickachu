from django.shortcuts import render
from django.views.generic import View


class Home(View):
    template_name = 'home/home_page.html'

    def get(self, request):
        context = {}

        return render(request, self.template_name, context)
