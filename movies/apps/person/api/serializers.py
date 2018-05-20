from rest_framework import serializers
from apps.person.models import Person, Alias


class AliasSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(
        required=True, allow_blank=False, max_length=Alias.MAXLENGTHDEFAULT)

    def create(self, validated_data):
        return Alias.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('name', instance.name)
        instance.save()
        return instance

    def validate_name(self, value):
        qs = Alias.objects.filter(name=value)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
            if qs.exists():
                raise serializers.ValidationError(
                    "The name and last name has already been registered")
            return(value)

class PersonSerializer(serializers.Serializer):
    # from apps.movie.api.serializers import MovieSerializer

    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(
        required=True, allow_blank=False, max_length=Person.MAXLENGTHDEFAULT)
    last_name = serializers.CharField(
        required=True, allow_blank=False, max_length=Person.MAXLENGTHDEFAULT)

    aliases = AliasSerializer(many=True, required=False)

    movies_as_director = serializers.SerializerMethodField()
    movies_as_actor = serializers.SerializerMethodField()
    movies_as_producer = serializers.SerializerMethodField()
   
    def get_movies_as_director(self, obj):
        from apps.movie.api.serializers import MovieUnrelatedSerializer
        return [MovieUnrelatedSerializer(movie).data for movie
            in obj.movies_as_director.all()]

    def get_movies_as_actor(self, obj):
        from apps.movie.api.serializers import MovieUnrelatedSerializer
        return [MovieUnrelatedSerializer(movie).data for movie
            in obj.movies_as_actor.all()]

    def get_movies_as_producer(self, obj):
        from apps.movie.api.serializers import MovieUnrelatedSerializer
        return [MovieUnrelatedSerializer(movie).data for movie
            in obj.movies_as_producer.all()]

    def create(self, validated_data):
        return Person.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get(
            'first_name', instance.first_name)
        instance.last_name = validated_data.get(
            'last_name', instance.last_name)
        instance.aliases = validated_data.get('aliases', instance.aliases)
        instance.save()
        return instance

    def validate(self, data):
        qs = Person.objects.filter(
            first_name__iexact=data['first_name'], 
            last_name__iexact=data['last_name'])
        if self.instance:
            qs = qs.exclude(pk=self.instance.id)
            if qs.exists():
                raise serializers.ValidationError(
                    "The name and last name has already been registered")
        return(data)
