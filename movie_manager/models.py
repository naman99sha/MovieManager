from django.db import models
from django.conf import settings
# Create your models here.
class Entry(models.Model):
	moviePoster=models.ImageField(upload_to='uploads')
	movieName=models.CharField(max_length=100)
	movieDescription=models.TextField(blank=True)
	createdDate=models.DateField(auto_now_add=True)
	releaseDate=models.DateField()

	def __str__(self):
		return self.movieName