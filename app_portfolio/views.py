from django.shortcuts import render
from django.views.generic import View

# Create your views here.
class CreatePageView(View):

    def get(self, request):
        return render(request=request, template_name="app_portfolio/modelo_1.html")