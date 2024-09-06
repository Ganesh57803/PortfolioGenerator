from django.db import models

# Create your models here.
from django.db import models

class UserDetails(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField()
    skills = models.TextField()
