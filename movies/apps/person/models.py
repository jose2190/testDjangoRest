# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Alias(models.Model):
    """Model definition for Alias."""
    MAXLENGTHDEFAULT = 50

    id = models.AutoField(primary_key=True)
    name = models.CharField(
        null=False, blank=False, max_length=MAXLENGTHDEFAULT)
    created_at = models.DateTimeField(null=False, auto_now=True)
    changed_at = models.DateTimeField(null=False, auto_now_add=True)

    class Meta:
        """Meta definition for Alias."""
        unique_together = ('name',)
        verbose_name = 'Alias'
        verbose_name_plural = 'Aliass'

    def __str__(self):
        """Unicode representation of Alias."""
        return(self.name)


class Person(models.Model):
    """Model definition for Person."""
    MAXLENGTHDEFAULT = 50
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(null=False, max_length=MAXLENGTHDEFAULT)
    last_name = models.CharField(null=False, max_length=MAXLENGTHDEFAULT)
    movies_as_director = models.ManyToManyField(
        'movie.Movie', related_name="movies_as_director")
    movies_as_actor = models.ManyToManyField(
        'movie.Movie', related_name="movies_as_actor")
    movies_as_producer = models.ManyToManyField(
        'movie.Movie', related_name="movies_as_producer")
    aliases = models.ManyToManyField(Alias, related_name='aliases')

    def save(self, *args, **kwargs):
        self.first_name = self.first_name.replace(',', '')
        self.last_name = self.last_name.replace(',', '')
        super(Person, self).save(*args, **kwargs)

    class Meta:
        """Meta definition for Person."""
        # app_label = 'Person'
        unique_together = ('first_name', 'last_name')
        verbose_name = 'Person'
        verbose_name_plural = 'Persons'

    def __str__(self):
        """Unicode representation of Person."""
        return("%s,%s" % (self.first_name, self.last_name))
