from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.TextField(blank = False,null = False)
    
    class Meta:
        ordering = ['user']

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}' 


