from django.db import models
from reg.models import Profile
from django.urls import reverse


class ChatGroup(models.Model):
    name = models.CharField(max_length = 255)
    members = models.ManyToManyField(Profile)
    is_personal_chat = models.BooleanField(default = False)
    admin = models.ForeignKey(Profile, on_delete = models.CASCADE, related_name = 'administered_group', null = True)
    avatar = models.ImageField(upload_to = "imgs/group_avatars", blank = True, null = True)
    
    def __str__(self):
        return f'Група ---> {self.name}'
    
    def get_absolute_url(self):
        return reverse("group", kwargs={"group_pk": self.pk})
    
class PersonalChat(models.Model):
    name = models.CharField(max_length = 255)
    members = models.ManyToManyField(Profile)
    avatar = models.ImageField(upload_to = "imgs/group_avatars", blank = True, null = True)
    
    def __str__(self):
        return f'Чат ---> {self.name}'
    
    def get_absolute_url(self):
        return reverse("chat", kwargs={"group_pk": self.pk})


class ChatMessage(models.Model):
    content = models.TextField(max_length = 4096)
    author = models.ForeignKey(Profile, on_delete = models.CASCADE)
    chat_group = models.ForeignKey(ChatGroup, on_delete = models.CASCADE)
    sent_at = models.DateTimeField(auto_now_add = True)
    attached_image = models.ImageField(upload_to = "imgs/messages", blank = True, null = True)

    view_by_users = models.ManyToManyField(Profile, related_name = "views")