from rest_framework import serializers
from .models import Character, Family, Incident, Region


# 캐릭터 전체 받아오기 용 serializer
class CharacterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Character
        fields = '__all__'
