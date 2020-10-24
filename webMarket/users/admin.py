from django.contrib import admin

# from .models import users
from .models import User, RegistrationDetail, Post
# Register your models here.
admin.site.register(User)
admin.site.register(RegistrationDetail)
admin.site.register(Post)