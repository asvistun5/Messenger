"""
URL configuration for Messenger project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from . import settings

from login.views import authorization, LogOutView
from reg.views import registration
from home.views import HomeView
from settings_app.views import SettingsView
from my_publications.views import CreatePublicationView
from settings_app.views import update_profile, AlbumsView
from friends_app.views import FriendsView
from user_app.views import ProfileView
from chat.views import ChatView, PersonalChatView, GroupChatView, redirect_to_personal_chat


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name = 'home'),
    path('register/', registration, name = 'reg'),
    path('login/', authorization, name = 'auth'),
    path('log-out/', LogOutView.as_view(), name = 'logout'),
    path('create/', CreatePublicationView.as_view(), name = 'create'),
    path('settings/', SettingsView.as_view(), name = 'settings'),
    path('albums/', AlbumsView.as_view(), name = 'albums'),
    path('update-profile/', update_profile, name='profile'),
    path('friends/', FriendsView.as_view(), name='friends'),
    path('profile/<int:id>/', ProfileView.as_view(), name='profile'),

    path('chats/', ChatView.as_view(), name = 'chats'),
    path('chat/<int:group_pk>', PersonalChatView.as_view(), name = 'personal'),
    path('group/<int:group_pk>', GroupChatView.as_view(), name = 'group'),
    path(route= 'to_personal/<int:user1_pk>/<int:user2_pk>', view= redirect_to_personal_chat, name= 'to_personal'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)