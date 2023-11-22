import folium
import json

from datetime import datetime
from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Pokemon, PokemonEntity

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
        add_pokemon(
            folium_map, pokemon_entity.lat,
            pokemon_entity.len,
            request.build_absolute_uri() 
        )
    
    pokemons = Pokemon.objects.all()

    pokemons_on_page = []
    for pokemon in pokemons:
        pokemons_on_page.append({
            'pokemon_id': pokemon.id,
            'img_url': f'media/{pokemon.image}',
            'title_ru': pokemon.title,
        })

    return render(request, 'mainpage.html', context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    
    pokemon = get_object_or_404(Pokemon, id=int(pokemon_id))

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    pokemon_entitys = PokemonEntity.objects.filter(pokemon=pokemon)
    pokemon_evolution = ""
    if pokemon.previous_evol.all():
        pokemon_evolution = pokemon.previous_evol.all()[0]

    for pokemon_entity in pokemon_entitys:
        add_pokemon(
            folium_map, pokemon_entity.lat,
            pokemon_entity.len,
            f'media/{pokemon_entity.pokemon.image}'
        )

    return render(request, 'pokemon.html', context={
        'map': folium_map._repr_html_(), 'pokemon': pokemon, 'pokemon_evol': pokemon_evolution
    })
