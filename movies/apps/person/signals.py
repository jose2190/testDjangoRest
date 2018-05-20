from django.db.models.signals import m2m_changed, post_save
from django.dispatch import receiver
from apps.movie.models import Movie
from apps.person.models import Person


@receiver(m2m_changed, sender=Movie.directors.through)
@receiver(m2m_changed, sender=Movie.casting.through)
@receiver(m2m_changed, sender=Movie.producers.through)
def update_person_movies(sender, instance, action, **kwargs):
    """When m2m changes."""
    instance = Movie.objects.get(id=instance.id)
    if action in ['post_add', 'post_remove', 'post_clear']:
        for p in Person.objects.filter(
            movies_as_director=instance).exclude(
                id__in=instance.directors.values_list('id', flat=True)):
            p.movies_as_director.remove(instance)
        for p in Person.objects.filter(
            movies_as_producer=instance).exclude(
                id__in=instance.producers.values_list('id', flat=True)):
            p.movies_as_producer.remove(instance)
        for p in Person.objects.filter(
            movies_as_actor=instance).exclude(
                id__in=instance.casting.values_list('id', flat=True)):
            p.movies_as_actor.remove(instance)
    assignMovies(instance)


@receiver(post_save, sender=Movie)
def add_movies(sender, instance, created, **kwargs):
    if created:
        assignMovies(instance)


def assignMovies(movie):
    for person in movie.directors.all():
            person.movies_as_director.add(movie)
    for person in movie.casting.all():
        person.movies_as_actor.add(movie)
    for person in movie.producers.all():
        person.movies_as_producer.add(movie)
