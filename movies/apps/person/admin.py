# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Person, Alias


# Register your models here.
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    '''Admin View for Person'''
    exclude = ('movies_as_director', 'movies_as_producer', 'movies_as_actor')

    list_display = ('first_name', 'last_name',)
    list_filter = ('movies_as_director',)
    search_fields = ('first_name', 'last_name')
    ordering = ('first_name', 'last_name')


@admin.register(Alias)
class AliasAdmin(admin.ModelAdmin):
    '''Admin View for Alias'''
    list_display = ('name',)
    search_fields = ('name',)
   