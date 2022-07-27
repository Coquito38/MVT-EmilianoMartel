from django.db import models

class Family(models.Model):
    name= models.CharField(max_length=50)
    birthay= models.DateField(auto_now_add=True, null=True, blank=True)
    age= models.IntegerField()