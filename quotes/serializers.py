from rest_framework import serializers
from .models import Personality


class PersonalitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Personality
        fields = ("pk", "personality_name", "url", "slug", "info", "trivia")
        read_only_fields = ("pk", "url", "slug")
