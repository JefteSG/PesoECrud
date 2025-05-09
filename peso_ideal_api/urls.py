"""
URL configuration for peso_ideal_api project.

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
from django.urls import path, re_path
from api.views import PessoaViewSet
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Peso Ideal API",
      default_version='v1',
      description="API para calcular peso ideal",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls), 
    path('api/v1/pessoa/', PessoaViewSet.as_view({'get': 'pesquisar', 'post': 'incluir'})),  
    path('api/v1/pessoa/<int:id>/', PessoaViewSet.as_view({'put': 'alterar', 'delete': 'excluir'})),
    path('api/v1/calcular_peso_ideal', PessoaViewSet.as_view({'post': 'calcular_peso_ideal'})), 
    re_path(r'^docs/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
