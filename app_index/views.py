from typing import Any
from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView, View

from easyportfolionow.mydecorators import LogoutRequiredMixin

# Create your views here.
def index(request):
    return render(request, 'app_index/index.html')


class IndexView(LogoutRequiredMixin, View):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__('/portfolio/perfil/')
        self.template_name = 'app_index/index.html'

    def get(self, request):
        search_portifolio = request.GET.get('search_portifolio')
        return render(request=request, template_name=self.template_name)

    def post(self, request):
        return HttpResponse('200')