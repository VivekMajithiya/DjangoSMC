from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class ChatData(models.Model):

    name = models.CharField(max_length=5)
    text = models.CharField(max_length=500)
    sentat = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name+':'+self.text+':'+str(self.sentat)

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    #additional fields
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return(self.user.username)
