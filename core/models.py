from django.db import models
import uuid
from django.contrib.auth import get_user_model


User = get_user_model()

# Create your models here.
class User_Profile(models.Model):
    user =models.ForeignKey(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null = True, max_length= 250)
    profileimg = models.ImageField(upload_to='profile_images', default='')
    location = models.CharField(max_length=100, blank=True, null= True)

    def __str__(self):
        return self.username 
    
class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False )
    user = models.CharField(max_length= 100)
    image = models.ImageField(upload_to='post_images')
    caption = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    num_of_likes = models.IntegerField(default=0)

    def __str__(self):
        return self.user 

