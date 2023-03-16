from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Eatery(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author =  models.ForeignKey(User, on_delete=models.CASCADE)

# class UserProfile(models.Model):
# 	PUBLIC = 'Public'
# 	PRIVATE = 'Private'
# 	TYPE_CHOICES = [
# 		(PUBLIC, 'Public'),
# 		(PRIVATE, 'Private'),
#     ]

# 	user = models.OneToOneField(User, on_delete=models.CASCADE)
# 	school_name = models.CharField(max_length=40)
# 	logo = models.ImageField(default='default.jpg', upload_to='logo_pics')
# 	banner = models.ImageField(upload_to='media', default='banner.jpg')
# 	location = models.CharField(max_length=200, default='')
# 	type = models.CharField(max_length=7, choices=TYPE_CHOICES, default=PUBLIC)
# 	email = models.EmailField(default = '')
# 	contact_details = models.TextField()
# 	mapbox_key = models.CharField(max_length=100)
# 	live_chat_link = models.CharField(max_length=50)
# 	chatbot_tree_link = models.CharField(max_length=50)
	
# 	def __str__(self):
# 		return self.school_name

    

