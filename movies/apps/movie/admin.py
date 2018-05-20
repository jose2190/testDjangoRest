# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    '''Admin View for Movie'''
    list_display = ('title', 'release_year')
    list_filter = ('release_year',)
    search_fields = ('title',)
    ordering = ('created_at',)
