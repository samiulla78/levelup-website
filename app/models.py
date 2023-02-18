from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Student(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=250)
    last_name= models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    phone =models.PositiveIntegerField()
    

    def __str__(self):
        return self.first_name

class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    auth_token=models.CharField(max_length=100)
    is_verified = models.BooleanField(default=False)
    created_at =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

# from django.db import models

# class Email(models.Model):
#     email = models.EmailField()
#     created_at = models.DateTimeField(auto_now_add=True)
