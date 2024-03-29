# Generated by Django 4.1.7 on 2023-05-24 21:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("userdashboard", "0004_alter_profile_profile_picture"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="eatery",
            name="food_genre",
        ),
        migrations.CreateModel(
            name="Menu",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("content", models.TextField()),
                ("price", models.IntegerField(blank=True, null=True)),
                (
                    "date_posted",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="eatery",
            name="menu_items",
            field=models.ManyToManyField(to="userdashboard.menu"),
        ),
    ]
