from django.db.models import Q
from rest_framework import generics, mixins

from apps.movie.models import Movie
from .serializers import MovieSerializer


class MovieAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = MovieSerializer

    def get_queryset(self):
        qs = Movie.objects.all()
        query = self.request.GET.get('q', None)
        if query is not None:
            qs = qs.filter(title__icontains=query).distinct()
        return(qs)

    def perform_create(self, serializer):
        """ Modified to use a custom serializer in create method"""
        return serializer.save()

    def create(self, request, *args, **kwargs):
        from apps.movie.api.serializers import MovieForViewSerializer
        from rest_framework.response import Response
        from rest_framework import status
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # Using modified method perform_created
        # if it's needed to use normal (from the library) method
        # a new implementation of the serializer was to be created
        model_object = self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            MovieForViewSerializer(model_object).data,
            status=status.HTTP_201_CREATED,
            headers=headers)

    def list(self, request, *args, **kwargs):
        """ Used to retreive custom view for movies,
            in this case for view release_year in roman numbers,
            and full document in persons across differents roles
        """
        from apps.movie.api.serializers import MovieForViewSerializer
        from rest_framework.response import Response
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = MovieForViewSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = MovieForViewSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        from apps.movie.api.serializers import MovieForViewSerializer
        from rest_framework.response import Response
        instance = self.get_object()
        serialized = MovieForViewSerializer(instance)
        return Response(serialized.data)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


class MovieRUDView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = MovieSerializer

    def retrieve(self, request, *args, **kwargs):
        from apps.movie.api.serializers import MovieForViewSerializer
        from rest_framework.response import Response
        instance = self.get_object()
        serialized = MovieForViewSerializer(instance)
        return Response(serialized.data)
   
    def get_queryset(self):
        return Movie.objects.all()

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}
