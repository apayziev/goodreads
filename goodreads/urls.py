"""goodreads URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.schemas import get_schema_view # new
from rest_framework.documentation import include_docs_urls # new
from rest_framework_swagger.views import get_swagger_view # new


API_TITLE = 'Goodreads API'
schema_view = get_swagger_view(title=API_TITLE) # new

from .views import landing_page, home_page

urlpatterns = [
    path('users/', include('users.urls')),
    path('books/', include('books.urls')),
    path('', landing_page, name='landing_page'),
    path('home/', home_page, name='home_page'),
    path('api/', include('api.urls')),


    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls'), name='accounts'),
    path('docs/', include_docs_urls(title='Goodreads API')), # new
    # path('schema/', schema_view), # new
    path('swagger-docs/', schema_view), # new
]

urlpatterns += static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)
