from __future__ import unicode_literals

from django.db import models
from django_extensions.db.models import TitleSlugDescriptionModel, TimeStampedModel
# Create your models here.


class Movies(TitleSlugDescriptionModel, TimeStampedModel):
    """ Movie model to store all the information related to a movie """
    imdb_score = models.DecimalField(decimal_places=3, max_digits=20, null=True, blank=True)
    genre = models.CharField(null=True, blank=True, max_length=200)
    director = models.CharField(null=True, blank=True, max_length=200)
    popularity_score = models.DecimalField(decimal_places=3, max_digits=20, null=True, blank=True)


    # objects = MoviesQuerySet.as_manager()
    def __str__(self):
        return self.title

