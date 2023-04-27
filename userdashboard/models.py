from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image


class Eatery(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    eatery_name = models.CharField(max_length=100)
    food_genre = models.CharField(max_length=200, default='', blank=True)
    details = models.TextField(blank=True)
    location = models.CharField(max_length=200, default='')
    logo = models.ImageField(default='eatery_logos/default.png', upload_to='eatery_logos')
    banner = models.ImageField(default='eatery_banners/banner.jpg', upload_to='eatery_banners')
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.eatery_name
    # Resize the logo
    def save(self, *args, **kwargs):
        super(Eatery, self).save(*args, **kwargs)
        img = Image.open(self.logo.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.logo.path)

