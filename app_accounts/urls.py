from django.urls import path
from .views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("cadastro/", view=CadastroView.as_view(), name="cadastro"),
    path("logar/", view=logar, name="logar"),
    path("sair/", view=sair, name="sair"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
