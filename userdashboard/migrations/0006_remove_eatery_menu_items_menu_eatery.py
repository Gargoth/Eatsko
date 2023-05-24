# Generated by Django 4.1.7 on 2023-05-24 21:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("userdashboard", "0005_remove_eatery_food_genre_menu_eatery_menu_items"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="eatery",
            name="menu_items",
        ),
        migrations.AddField(
            model_name="menu",
            name="eatery",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="userdashboard.eatery",
            ),
        ),
    ]
