from django.contrib import admin
from .models import ChatGroup, ChatMessage, PersonalChat

admin.site.register(ChatGroup)
admin.site.register(ChatMessage)
admin.site.register(PersonalChat)