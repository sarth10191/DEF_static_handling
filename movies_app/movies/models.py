from django.db import models

# Create your models here.
class Moviedata(models.Model):

    def __str__(self) -> str:
        return self.name
    
    name = models.CharField(max_length=200)
    duration = models.FloatField()
    rating = models.FloatField()
    category = models.CharField(max_length=200, default="Thriller")
    image = models.ImageField(upload_to='Images/', default='Images/None/noimg.jpg')


