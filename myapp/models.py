from django.db import models

# Create your models here.
class Library(models.Model):
    name = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    def __str__(self):
	    return self.name
class Review(models.Model):
    name = models.CharField(max_length=200,null= True)
    address = models.CharField(max_length=200,null=True)
    review = models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.name