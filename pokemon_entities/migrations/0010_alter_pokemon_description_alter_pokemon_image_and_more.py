# Generated by Django 4.2.4 on 2023-09-03 19:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0009_pokemon_next_evolution_pokemon_previous_evolution'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='pokemons_img', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='next_evolution',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='next_evol', to='pokemon_entities.pokemon', verbose_name='В кого эволюционирует'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='previous_evolution',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='previous_evol', to='pokemon_entities.pokemon', verbose_name='Из кого иволюционировал'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Название на русском'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='title_en',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Название на Англиском'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='title_jp',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Название на Японском'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='appeared_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата появления'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='defence',
            field=models.IntegerField(blank=True, null=True, verbose_name='Защита'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='disappered_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата исчезновения'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='health',
            field=models.IntegerField(blank=True, null=True, verbose_name='Здоровье'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='lat',
            field=models.FloatField(verbose_name='Широта'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='len',
            field=models.FloatField(verbose_name='Долгота'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='level',
            field=models.IntegerField(blank=True, null=True, verbose_name='Уровень'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='pokemon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pokemon_entities.pokemon', verbose_name='Покемон'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='stamina',
            field=models.IntegerField(blank=True, null=True, verbose_name='Выносливость'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='strength',
            field=models.IntegerField(blank=True, null=True, verbose_name='Сила'),
        ),
    ]
