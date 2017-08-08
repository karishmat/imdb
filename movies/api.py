__author__ = 'karishma'

from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.decorators import renderer_classes
from rest_framework import viewsets

from .serializers import MovieSerializer
from .models import Movies


class MovieViewSet(viewsets.ModelViewSet):

    queryset = Movies.objects.all()
    serializer_class = MovieSerializer
    renderer_classes = (TemplateHTMLRenderer,)

    def list(self, request, *args, **kwargs):
        response = super(MovieViewSet, self).list(request, *args, **kwargs)
        if request.accepted_renderer.format == 'html':
            return Response({'movie_list': response.data}, template_name='movies.html')
        return response

    def retrieve(self, request, *args, **kwargs):
        response = super(MovieViewSet, self).retrieve(request, *args, **kwargs)
        if request.accepted_renderer.format == 'html':
            return Response({'movie_detail': response.data}, template_name='movie_detail.html')
        return response

