# Generated by Django 3.2.10 on 2022-01-09 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='allergydrink',
            old_name='allergy_id',
            new_name='allergy',
        ),
        migrations.RenameField(
            model_name='allergydrink',
            old_name='drink_id',
            new_name='drink',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='menu_id',
            new_name='menu',
        ),
        migrations.RenameField(
            model_name='drink',
            old_name='category_id',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='image',
            old_name='drink_id',
            new_name='drink',
        ),
        migrations.RenameField(
            model_name='nutrition',
            old_name='drinks_id',
            new_name='drinks',
        ),
        migrations.RenameField(
            model_name='nutrition',
            old_name='size_id',
            new_name='size',
        ),
        migrations.AddField(
            model_name='allergy',
            name='allergy_drink',
            field=models.ManyToManyField(through='products.AllergyDrink', to='products.Drink'),
        ),
    ]
