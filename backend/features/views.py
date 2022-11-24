from .models import Character, Family, Incident, Region
from .serializers import CharacterSerializer
from django.shortcuts import render, get_list_or_404, get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.


@api_view(['GET', 'POST'])
def character_list(request):

    def get_characters():
        valars = get_list_or_404(Character, race='valar')
        elves = get_list_or_404(Character, race='elf')
        humans = get_list_or_404(Character, race='human')
        dwarves = get_list_or_404(Character, race='dwarf')
        hobbits = get_list_or_404(Character, race='hobbit')
        orcs = get_object_or_404(Character, race='orc')
        others = get_object_or_404(Character, race='other')

        valars_serializer = CharacterSerializer(valars, many=True)
        elves_serializer = CharacterSerializer(elves, many=True)
        humans_serializer = CharacterSerializer(humans, many=True)
        dwarves_serializer = CharacterSerializer(dwarves, many=True)
        hobbits_serializer = CharacterSerializer(hobbits, many=True)
        orcs_serializer = CharacterSerializer(orcs)
        othres_serializer = CharacterSerializer(others)

        valars_data = valars_serializer.data
        elves_data = elves_serializer.data
        humnas_data = humans_serializer.data
        dwarves_data = dwarves_serializer.data
        hobbits_data = hobbits_serializer.data
        orcs_data = orcs_serializer.data
        others_data = othres_serializer.data

        response_data = {"valars": valars_data, "elves": elves_data, "humans": humnas_data,
                         "dwarves": dwarves_data, "hobbits": hobbits_data, "orcs": orcs_data, "others": others_data}
        return Response(response_data)

    def post_characters():
        serializer = CharacterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({'saved': True})

    if request.method == 'GET':
        return get_characters()
    elif request.method == 'POST':
        return post_characters()


@api_view(['GET'])
def get_race_list(request, race_name):

    def tmp_one():
        races = get_list_or_404(Character, race=race_name)
        serializer = CharacterSerializer(races, many=True)
        return Response(serializer.data)

    def tmp_two():
        race = get_object_or_404(Character, race=race_name)
        serializer = CharacterSerializer(race)
        return Response(serializer.data)

    if race_name in ['valar', 'human', 'elf', 'dwarf', 'hobbit']:
        return tmp_one()
    else:
        return tmp_two()
        

@api_view(['GET'])
def get_character_detail(request, character):
    character = get_object_or_404(Character, name=character)
    serializer = CharacterSerializer(character)
    return Response(serializer.data)