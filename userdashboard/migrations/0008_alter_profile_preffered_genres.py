# Generated by Django 4.1.7 on 2023-05-25 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userdashboard', '0007_profile_eatery_alter_menu_eatery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='preffered_genres',
            field=models.ManyToManyField(blank=True, to='userdashboard.foodgenre'),
        ),
    ]
