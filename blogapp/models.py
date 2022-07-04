from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

class Post(models.Model):
	image = CloudinaryField('image')
	title = models.CharField(max_length = 200)
	body = models.TextField()
	slug = models.SlugField()
	writer = models.ForeignKey(User, on_delete = models.CASCADE)
	created_on = models.DateTimeField(auto_now = True)

	def __str__(self):
		return self.title


class Comment(models.Model):
    commenter = models.CharField(max_length = 50)
    body = models.TextField()
    post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name='comments')
    
    def __str__(self):
        return self.body