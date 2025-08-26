"""
URL configuration for agendamentos_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from accounts import views as accounts_views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

#doumentação por endpoint
schema_view = get_schema_view(
    openapi.Info(
        title="API de Agendas",
        default_version='v1',
        description="Documentação da API de gerenciamento de agendas",
        contact=openapi.Contact(email="vitorquaresmadasilva@gmail.com"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    #rotas do projeto
    path('admin/', admin.site.urls), #rota de controle dos admins 
    path('accounts/', include('django.contrib.auth.urls')), #rota de login/logout
    path("signup/", accounts_views.signup, name="signup"), #rota de novo usuario
    path('api/', include('agendas.urls')),
    # urls de documentação
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),# Swagger UI
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'), # Redoc UI
]