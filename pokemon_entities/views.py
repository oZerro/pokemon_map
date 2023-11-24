import folium
import json

from datetime import datetime
from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Pokemon, PokemonEntity
from pogomap.settings import MEDIA_URL

MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = (
    'https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision'
    '/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832'
    '&fill=transparent'
)


def add_pokemon(folium_map, lat, lon, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    now_date = datetime.now()
    pokemon_entities = PokemonEntity.objects.filter(disappered_at__gt=now_date, appeared_at__lte=now_date)
    
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    
    for pokemon_entity in pokemon_entities:
        image_path = f'{MEDIA_URL}{pokemon_entity.pokemon.image}'
        absolute_uri_image = request.build_absolute_uri(image_path)

        add_pokemon(
            folium_map, pokemon_entity.lat,
            pokemon_entity.len,
            absolute_uri_image
        )
    
    pokemons = Pokemon.objects.all()

    pokemons_on_page = []
    for pokemon in pokemons:
        image_path = f'{MEDIA_URL}{pokemon.image}'
        absolute_uri_image = request.build_absolute_uri(image_path)
        pokemons_on_page.append({
            'pokemon_id': pokemon.id,
            'img_url': absolute_uri_image,
            'title_ru': pokemon.title,
        })

    return render(request, 'mainpage.html', context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    
    pokemon = get_object_or_404(Pokemon, id=int(pokemon_id))

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    pokemon_entities = PokemonEntity.objects.filter(pokemon=pokemon)
    
    pokemon_evolution = pokemon.next_evolutions.first()

    for pokemon_entity in pokemon_entities:
        image_path = f'{MEDIA_URL}{pokemon_entity.pokemon.image}'
        absolute_uri_image = request.build_absolute_uri(image_path)
        add_pokemon(
            folium_map, pokemon_entity.lat,
            pokemon_entity.len,
            absolute_uri_image
            
        )

    return render(request, 'pokemon.html', context={
        'map': folium_map._repr_html_(), 'pokemon': pokemon, 'next_evolutions': pokemon_evolution
    })
