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
        # Warning! `tooltip` attribute is disabled intentionally
        # to fix strange folium cyrillic encoding bug
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    now_date = datetime.now()
    pokemon_entitys = PokemonEntity.objects.filter(disappered_at__gt=now_date, appeared_at__lte=now_date)
    
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    
    for pokemon_entity in pokemon_entitys:
        add_pokemon(
            folium_map, pokemon_entity.lat,
            pokemon_entity.len,
            f'media/{pokemon_entity.pokemon.image}'
        )
    
    pokemons2 = Pokemon.objects.all()

    pokemons_on_page = []
    for pokemon in pokemons2:
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
    try:
        pokemon = get_object_or_404(Pokemon, id=int(pokemon_id))
    except Exception as ex:
        return HttpResponseNotFound('<h1>Такой покемон не найден</h1>')

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    pokemon_entitys = PokemonEntity.objects.filter(pokemon=pokemon)
    for pokemon_entity in pokemon_entitys:
        add_pokemon(
            folium_map, pokemon_entity.lat,
            pokemon_entity.len,
            f'media/{pokemon_entity.pokemon.image}'
        )

    return render(request, 'pokemon.html', context={
        'map': folium_map._repr_html_(), 'pokemon': pokemon
    })
