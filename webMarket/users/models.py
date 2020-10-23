from django.db import models
# Create your models here.
class User(models.Model):
    first_name = models.TextField(null = False)
    last_name = models.TextField(null = False)
    email = models.EmailField(null = False)
    password = models.TextField(null = False)
    re_password = models.TextField(null = False)
    phone_number = models.TextField(null = False)
    
