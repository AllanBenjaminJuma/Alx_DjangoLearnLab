from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # definition of the new fields to be added apart from already existing username, fname, lname, password
    bio = models.TextField(max_length=500, blank=True, null = True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    followers = models.ManyToManyField('self', related_name='following', symmetrical=False, blank=True)
    
    def __str__(self):
        return self.username