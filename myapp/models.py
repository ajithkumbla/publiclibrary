from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#library model

class Library(models.Model):
    name = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    def __str__(self):
	    return self.name

#post model

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)
 
class Post(models.Model):
    library = models.ForeignKey(Library,on_delete= models.CASCADE); 
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
