from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.TextField(blank = False,null = False)
    last_name = models.TextField(blank = False,null = False)
    email = models.EmailField(blank = False,null = False)
    password = models.TextField(blank = False,null = False)
    phone_number = models.TextField(blank = False,null = False)
    picture = models.ImageField(blank = True,null = True)

    class Meta:
        ordering = ['last_name','first_name','email']

    def __str__(self):
        return f'{self.first_name} {self.last_name}' 


