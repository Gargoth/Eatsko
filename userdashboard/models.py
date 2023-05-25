from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image


class FoodGenre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'


class Eatery(models.Model):
    eatery_name = models.CharField(max_length=100)
    food_genres = models.ManyToManyField(FoodGenre)
    details = models.TextField(blank=True)
    location = models.CharField(max_length=200, default='')
    logo = models.ImageField(default='eatery_logos/default.png', upload_to='eatery_logos')
    banner = models.ImageField(default='eatery_banners/banner.jpg', upload_to='eatery_banners')
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.eatery_name}'

    # Resize the logo
    def save(self, *args, **kwargs):
        super(Eatery, self).save(*args, **kwargs)
        img = Image.open(self.logo.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.logo.path)


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE, related_name='user_profile')
    account_type = models.CharField(max_length=100, default='User')
    profile_picture = models.ImageField(default='profile_pics/default.png', upload_to='profile_pics')
    preffered_genres = models.ManyToManyField(FoodGenre, blank=True)
    eatery = models.ForeignKey(Eatery, null=True, on_delete=models.SET_NULL)

    @classmethod
    def create(cls, user, account_type):
        new_profile = cls(user=user, account_type=account_type)
        return new_profile

    def __str__(self):
        return f'{self.user.username}'

    # Resize the profile picture
    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
        img = Image.open(self.profile_picture.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.profile_picture.path)


class Menu(models.Model):
    title = models.CharField(max_length=100)
    eatery = models.ForeignKey(Eatery, on_delete=models.CASCADE, null=True, related_name='menuitems')
    content = models.TextField()
    price = models.IntegerField(null=True, blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('menu-detail', kwargs={'pk': self.pk})
