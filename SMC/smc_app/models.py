from django.db import models

# Create your models here.
class ChatData(models.Model):

    name = models.CharField(max_length=5)
    text = models.CharField(max_length=500)
    sentat = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name+':'+self.text+':'+str(self.sentat)
