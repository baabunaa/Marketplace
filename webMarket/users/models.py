from django.db import models
# Create your models here.
CATEGORIES = [
    ('HT', 'Home Technics'),
    ('EL', 'Electronics'),
    ('SP', 'Sports'),
    ('MA', 'Music & Art')
]


class RegistrationDetail(models.Model):
    first_name = models.TextField(blank = False,null = False)
    last_name = models.TextField(blank = False,null = False)
    email = models.EmailField(blank = False,null = False)
    password = models.TextField(blank = False,null = False)
    re_password = models.TextField(blank = False,null = False)
    phone_number = models.TextField(blank = False,null = False)

    
class User(models.Model):
    details = models.ForeignKey(RegistrationDetail,on_delete = models.CASCADE, null=False)



class Post(models.Model):
    name = models.TextField(blank = False,null = False)
    price = models.FloatField(blank = False,null = False)
    description = models.TextField(blank = True,null = False)
    category = models.CharField(max_length = 2,choices = CATEGORIES,blank = False, null = False)
    picture = models.ImageField(blank = False,null = True)
    user = models.ForeignKey(User,on_delete = models.CASCADE,related_name='posts')
