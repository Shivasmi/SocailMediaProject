from django.db import models
import uuid
from django.contrib.auth import get_user_model
from datetime import datetime

User = get_user_model()

# Create your models here.
class Profile(models.Model):
    user =models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    bio = models.TextField(blank=True, null = True, max_length= 250)
    profileimg = models.ImageField(upload_to='profile_images', default='blank-profile-picture.png')
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username 
    
class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False )
    user = models.CharField(max_length= 100)
    image = models.ImageField(upload_to='post_images')
    caption = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    num_of_likes = models.IntegerField(default=0)

    def __str__(self):
        return self.user 

class LikePost(models.Model):
    post_id = models.CharField(max_length=100)
    username= models.CharField(max_length=200)
    content=models.TextField(max_length=800)
    likes=models.ManyToManyField(User)

    def get_likes_count(self):
        return self.likes.count()
    
    def __str__(self):
        return self.username
    
class FollowersCount(models.Model):
    follower = models.CharField(max_length=100)
    user = models.CharField(max_length=100)
    
    def __str__(self):
        return self.user 
    
class UserAddressInformation(models.Model):
    user = models.CharField(max_length= 100)
    address = models.CharField(max_length= 300)

    def __str__(self):
        return self.address

class UserComment(models.Model):
    user = models.CharField(max_length =100)
    comment = models.CharField(max_length=300)

    def __str__(self):
        return self.comment
    

class Repost(models.Model):
    user_repost = models.TextField(max_length= 100, default= '', blank=True)
    original_post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='reposts')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} reposted {self.original_post}"
    

class Notification(models.Model):
    likepost= models.CharField(max_length=100)
    likeby = models.ManyToManyField(to=Post)
    
    def __str__(self):
        return f"{self.user.username} notification {self.likepost} likeby {self.user}"
    

        
    

 


    


