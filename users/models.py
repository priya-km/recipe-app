from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=120)
    pic = models.ImageField(upload_to='users', default='no_picture.jpg')
      
    def __str__(self):
        return self.name