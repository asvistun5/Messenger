from channels.generic.websocket import AsyncWebsocketConsumer
from .forms import MessageForm
from .models import ChatGroup, ChatMessage
from channels.db import database_sync_to_async
from asgiref.sync import sync_to_async
from reg.models import Profile

import json


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):

        self.room_group_name = str(self.scope['url_route']['kwargs']['group_pk']) 

        await self.channel_layer.group_add(

            self.room_group_name,
            self.channel_name
        )
        
        await self.accept()

    async def receive(self, text_data):

        message_db = await self.save_message_to_db(text_data = text_data)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'send_message_to_every_member',
                'text_data': text_data,
                "username": Profile.objects.get(user=self.scope['user']).username,
                "date_time": message_db.date_time,
                "message": message_db
            }
        )

    async def send_message_to_every_member(self, event):
        # Створюємо об'єкт форми для повідолмень та наповнює її даними
        form = MessageForm(json.loads(event['text_data']))
        #робимо перевірку форми
        try:
            #Якщо форма валідна 
            if form.is_valid():
                #Відправляємо повідомлення назад клієнту у форматі JSON
                # message = event['message'].view_by_users
                # for user in 
                # await print(event['message'].view_by_users.count())
                await self.send(text_data= json.dumps({
                    'type': 'chat',
                    'message': form.cleaned_data['message'], #текст повідомлення
                    'username': event["username"], # Отримуємо ім'я користувача, яке ми передали через метод receive та group_send
                    "date_time": event['date_time'].isoformat(),
                    "views": await self.get_views_count(event['message']),
                    "avatar": event['message'].author.image.url
                }))
        except Exception as ERROR:
            print(ERROR)

    @database_sync_to_async
    def save_message_to_db(self, text_data):
        '''
            Зберігає повідомлення у БД в асинхронному режимі
        '''
        #Створюємо новий об'єкт ChatMessage та зберігаємо його у БД
        return ChatMessage.objects.create(
            content = json.loads(text_data)["message"],#отримуємо текст повідомлення з json
            author = Profile.objects.get(user=self.scope['user']),#автор повідомлення - поточний користувач
            chat_group = ChatGroup.objects.get(pk = self.room_group_name)#група чату,до якої належать повідомлення 
        )
    @sync_to_async
    def get_views_count(self, message):
        return message.view_by_users.count()