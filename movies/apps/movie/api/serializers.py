from rest_framework import serializers
from apps.movie.models import Movie
from apps.person.models import Person
from apps.person.api.serializers import PersonSerializer


class MovieUnrelatedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'release_year')


class MovieSerializer(MovieUnrelatedSerializer):
    id = serializers.IntegerField(read_only=True)
    """Title of a Movie"""
    title = serializers.CharField(
        required=True, allow_blank=False, max_length=50)
    release_year = serializers.IntegerField(required=True)
    casting = serializers.PrimaryKeyRelatedField(
        many=True, read_only=False, queryset=Person.objects.all())
    directors = serializers.PrimaryKeyRelatedField(
        many=True, read_only=False, queryset=Person.objects.all())
    producers = serializers.PrimaryKeyRelatedField(
        many=True, read_only=False, queryset=Person.objects.all())

    class Meta(MovieUnrelatedSerializer.Meta):
        fields = (
            *MovieUnrelatedSerializer.Meta.fields, 
            'release_year',
            'casting',
            'directors',
            'producers')

    def create(self, validated_data):
        """
        Fix for Django 2.0 support for direct assignment in manytomany fields
        https://docs.djangoproject.com/en/2.0/releases/2.0/#features-removed-in-2-0)
        """
        movie = Movie()
        movie.title = validated_data['title']
        movie.release_year = validated_data['release_year']
        movie.save()
        movie.producers.set(validated_data['producers'])
        movie.directors.set(validated_data['directors'])
        movie.casting.set(validated_data['casting'])
        return movie

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.release_year = validated_data.get(
            'release_year', instance.release_year)
        instance.casting.set(validated_data.get(
            'casting', instance.casting))
        instance.directors.set(validated_data.get(
            'directors', instance.casting))
        instance.producers.set(validated_data.get(
            'producers', instance.casting))
        instance.save()

        return instance

    def validate(self, data):
        qs = Movie.objects.filter(title=data['title'])
        if self.instance:
            qs = qs.exclude(pk=self.instance.id)
            if qs.exists():
                raise serializers.ValidationError(
                    "The title has already been registered")
        if data['release_year'] > 3000:
            raise serializers.ValidationError(
                    "by API functionality, you can not"
                    "enter senior years to 3000"
                )
        return(data)


class MovieForViewSerializer(MovieSerializer):
    release_year = serializers.SerializerMethodField()
    casting = PersonSerializer(many=True, required=True)
    directors = PersonSerializer(many=True, required=True)
    producers = PersonSerializer(many=True, required=True)

    def get_release_year(self, obj):
        from libs.numbers import int_to_roman
        return(int_to_roman(obj.release_year))

    class Meta(MovieSerializer.Meta):
        model = Movie
        fields = (
            *MovieSerializer.Meta.fields, 
            'release_year',
            'casting',
            'directors',
            'producers',
            )