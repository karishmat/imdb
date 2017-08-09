"""imdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from movies.api import MovieViewSet
from movies.views import create_movie, update_movie, delete_movie
router = DefaultRouter()
router.register(r'movie', MovieViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/movie/create/', create_movie, name='create-movie'),
    url(r'^api/movie/update/(?P<id>\d+)', update_movie, name='update-movie'),
    url(r'^api/movie/delete/(?P<id>\d+)', delete_movie, name='delete-movie'),


]


urlpatterns += [
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/rest-auth/', include('rest_auth.urls'))

    ]
