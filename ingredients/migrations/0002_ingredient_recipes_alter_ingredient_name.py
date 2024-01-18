# Generated by Django 5.0.1 on 2024-01-18 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingredients', '0001_initial'),
        ('recipes', '0002_alter_recipe_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='recipes',
            field=models.ManyToManyField(related_name='ingredients', to='recipes.recipe'),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='name',
            field=models.CharField(max_length=31),
        ),
    ]
