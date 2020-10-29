from django.db import models
from users.models import User
# Create your models here.
CATEGORIES = [
    ('HT', 'Home Technics'),
    ('EL', 'Electronics'),
    ('SP', 'Sports'),
    ('MA', 'Music & Art')
]


class Post(models.Model):
    name = models.TextField(blank = False,null = False)
    price = models.FloatField(blank = False,null = False)
    description = models.TextField(blank = True,null = False)
    category = models.CharField(max_length = 2,choices = CATEGORIES,blank = False, null = False)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    picture = models.ImageField(blank = False,null = True)
    user = models.ForeignKey(User,on_delete = models.CASCADE,related_name='posts')

    class Meta:
        ordering = ['-date', '-time']

    def __str__(self):
        return f'{self.name} - {self.user} on {self.date} {self.time.replace(microsecond=0)}'