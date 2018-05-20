# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Movie(models.Model):
    """Model definition for Movie."""
    PERSONMODEL = 'person.Person'
    id = models.AutoField(primary_key=True)
    title = models.CharField(null=False, blank=False, max_length=50)
    release_year = models.IntegerField(null=False)
    casting = models.ManyToManyField(PERSONMODEL, related_name='casting')
    directors = models.ManyToManyField(PERSONMODEL, related_name='directors')
    producers = models.ManyToManyField(PERSONMODEL, related_name='producers')
    created_at = models.DateTimeField(auto_now_add=True)
    changed_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        super(Movie, self).save(*args, **kwargs)

    class Meta:
        """Meta definition for Movie."""
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'

    def __str__(self):
        """Unicode representation of Movie."""
        return self.title
