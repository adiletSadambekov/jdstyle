"""jd_tseh URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf.urls.static import static

# View classes
from core.views import ProductView, ApplicationCallView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/products/', ProductView.as_view()),
    path('api/v1/createApplicationCall/', ApplicationCallView.as_view()),
]

if settings.DEBUG:

    # schema_view = get_schema_view(
    #     openapi.Info(
    #         title="MChart API",
    #         default_version='v1',
    #         description="MChart Python API",
    #         terms_of_service="",
    #         contact=openapi.Contact(email="whoiam@gmail.com"),
    #     ),
    #     public=True,
    #     permission_classes=[permissions.AllowAny, ],
    # )
    # urlpatterns = urlpatterns + [
    #     path(r'api/v1/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # ]

    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

