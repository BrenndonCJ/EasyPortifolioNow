from django.urls import path
from . import views

urlpatterns = [
    # path("<username>/", view=views.PortfolioView.as_view(), name="portfolio"),
    path("view/<username>/", view=views.PortfolioView.as_view(), name="userportfolio"),
    path("perfil/", view=views.PerfilView.as_view(), name="userperfil"),
    path("perfil/projeto/add", view=views.add_projeto, name="addproject"),
    path("perfil/projeto/<int:id>/", view=views.remover_projeto, name="projectdelete"),

    path("perfil/portfolioselect/", view=views.PortfolioModelSelect.as_view(), name="portfolioselect"),
    path("perfil/portfoliocreate/<int:modelo>", view=views.PortfolioCreate.as_view(), name="portfoliocreate"),
    path("<username>/", view=views.PortfolioView.as_view(), name="portfolioview"),
    path("perfil/portfoliocreate/gerarlink/<username>", view=views.generate_link, name="generatelink"),
]
