from django.db import models  



class Pokemon(models.Model):
    title = models.CharField(
        max_length=200, 
        verbose_name="Название на русском",
        default="Покемон")
    title_en = models.CharField(
        max_length=200, 
        blank=True, 
        verbose_name="Название на Англиском")
    title_jp = models.CharField(
        max_length=200, 
        blank=True,
        verbose_name="Название на Японском")
    previous_evolution = models.ForeignKey(
        "Pokemon", 
        on_delete=models.SET_NULL, 
        related_name='next_evolutions',
        null=True,
        blank=True,
        verbose_name="Из кого иволюционировал")
    description = models.TextField(blank=True, verbose_name="Описание", default="Покемон")
    image = models.ImageField(
        upload_to='pokemons_img', 
        null=True, 
        blank=True,
        verbose_name="Изображение")


    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(
        Pokemon, 
        on_delete=models.CASCADE, 
        related_name='entities',
        null=True,
        verbose_name="Покемон")
    lat = models.FloatField(verbose_name="Широта")
    len = models.FloatField(verbose_name="Долгота")
    appeared_at = models.DateTimeField(
        null=True, 
        blank=True,
        verbose_name="Дата появления")
    disappered_at = models.DateTimeField(
        null=True, 
        blank=True,
        verbose_name="Дата исчезновения")
    level = models.IntegerField(
        null=True, 
        blank=True,
        verbose_name="Уровень")
    health = models.IntegerField(
        null=True, 
        blank=True,
        verbose_name="Здоровье")
    strength = models.IntegerField(
        null=True, 
        blank=True,
        verbose_name="Сила")
    defence = models.IntegerField(
        null=True, 
        blank=True,
        verbose_name="Защита")
    stamina = models.IntegerField(
        null=True,
        blank=True,
        verbose_name="Выносливость")

    def __str__(self):
        return f'{self.lat} {self.len}'
