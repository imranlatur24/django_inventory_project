from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class ProfileModel(models.Model):
    staff=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    address=models.TextField(max_length=200,default='None')
    phone=models.CharField(max_length=10,default='None')
    image=models.ImageField(default='profile_images/avatar.png',upload_to="profile_images")
    def __str__(self):
        return f'{self.staff.username}-Profile'

