# Generated by Django 4.1.7 on 2023-04-27 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("userdashboard", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="account_type",
            field=models.CharField(default="User", max_length=100),
        ),
    ]
