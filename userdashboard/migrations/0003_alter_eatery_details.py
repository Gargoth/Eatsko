# Generated by Django 4.1.7 on 2023-03-16 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userdashboard', '0002_alter_eatery_banner_alter_eatery_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eatery',
            name='details',
            field=models.TextField(blank=True),
        ),
    ]
