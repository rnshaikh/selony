"""
URL configuration for selony_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.csrf import csrf_exempt

from graphene_django.views import GraphQLView
from graphene_file_upload.django import FileUploadGraphQLView

from .schema import schema

from order_management.views import WebHookView

admin.site.site_header = "Selony Admin"
admin.site.site_title = "Selony Administration"
admin.site.index_title = "Welcome To Selony"

urlpatterns = [
    path('admin/', admin.site.urls),
    path("o/", include('oauth2_provider.urls'), name="oauth2_apps"),
    #path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),
    path('graphql/', csrf_exempt(FileUploadGraphQLView.as_view(graphiql=True, schema=schema))),
    path('order/webhook/', WebHookView.as_view(), name="stripe_webhook")
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
