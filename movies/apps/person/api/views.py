from django.db.models import Q
from rest_framework import generics, mixins

from apps.person.models import Person
from .serializers import PersonSerializer, AliasSerializer


class PersonAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = PersonSerializer

    def get_queryset(self):
        qs = Person.objects.all()
        query = self.request.GET.get('q', None)
        if query is not None:
            qs = qs.filter(
                Q(first_name__icontains=query)|
                Q(last_name__icontains=query),
            ).distinct()
        return(qs)

    def perform_create(self, serializer):
        serializer.create()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


class PersonRUDView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = PersonSerializer

    def get_queryset(self):
        return Person.objects.all()

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}
