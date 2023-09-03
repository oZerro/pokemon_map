from django.db import models  # noqa F401

# your models here


class Pokemon(models.Model):
    title = models.CharField(max_length=200)
    title_en = models.CharField(max_length=200, null=True, blank=True)
    title_jp = models.CharField(max_length=200, null=True, blank=True)
    next_evolution = models.ForeignKey(
        "Pokemon",
        on_delete=models.SET_NULL, 
        related_name='next_evol',
        null=True, 
        blank=True)
    previous_evolution = models.ForeignKey(
        "Pokemon", 
        on_delete=models.SET_NULL, 
        related_name='previous_evol',
        null=True,
        blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='pokemons_img', null=True, blank=True)


    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, null=True, blank=True)
    lat = models.FloatField()
    len = models.FloatField()
    appeared_at = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    disappered_at = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    level = models.IntegerField(null=True, blank=True)
    health = models.IntegerField(null=True, blank=True)
    strength = models.IntegerField(null=True, blank=True)
    defence = models.IntegerField(null=True, blank=True)
    stamina = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.lat} {self.len}'
