from django.db import models
from django.contrib.auth.models import User
from my_publications.models import User_Post
from friends_app.models import FriendRequest


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name = 'profile')
    where_active = models.BooleanField(default=False)
    image = models.ImageField(upload_to='user_images/', blank=True, null=True)
    posts = models.ManyToManyField(User_Post, related_name='posts', blank = True)
    followers = models.ManyToManyField(User, related_name='followers', blank = True)
    friends = models.ManyToManyField(User, related_name='friends', blank = True)

    #requests = models.ManyToManyField(FriendRequest, related_name='requests', default = 0) #blank = True
    #messages = models.ManyToManyField(User, related_name='msgs', default = 0) #blank = True


    def __str__(self):
        return self.user.username
    
class FriendShip(models.Model):
    profile1 = models.ForeignKey(Profile, on_delete = models.CASCADE, related_name = 'friendship_sent_request')
    profile2 = models.ForeignKey(Profile, on_delete = models.CASCADE, related_name = 'friendship_accepted_request')
    accepted = models.BooleanField(default = False)

class RegistrationCodes(models.Model):
    email = models.EmailField(unique=True)
    code = models.CharField(max_length=6)
