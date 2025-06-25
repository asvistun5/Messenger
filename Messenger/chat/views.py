from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, FormView
from django.http import HttpResponseForbidden
from .models import ChatGroup, ChatMessage, PersonalChat
from .forms import SearchPeopleForm
from django.urls import reverse
from django.db.models import OuterRef, Subquery
from reg.models import Profile
from .forms import MessageForm

def make_correct_ukr_members(count):
    if count == 1:
        return f"{count} учасник"
    elif 2 <= count % 10 <= 4 and not (12 <= count % 100 <= 14):
        return f"{count} учасники"
    else:
        return f"{count} учасників"

class ChatView(View):
    template_name = "chat.html"
    search_form = SearchPeopleForm

    def get(self, request, *args, **kwargs):
        profile = Profile.objects.filter(user=request.user).first()
        groups = ChatGroup.objects.filter(members=profile)
        personal_chats = PersonalChat.objects.filter(members=profile)

        last_messages_subquery = ChatMessage.objects.filter(
            chat_group=OuterRef('pk')
        ).order_by('-sent_at')


        groups = groups.annotate(
            last_message=Subquery(last_messages_subquery.values('content')[:1]),
            last_message_time=Subquery(last_messages_subquery.values('sent_at')[:1])
        )
        

        friends = Profile.objects.filter(user__in=profile.friends.all())

        context = {
            'form': self.search_form,
            'page': 'chat',
            'friends': friends,
            'groups': groups,
            'user_pk': profile.pk,
            'chats': personal_chats
        }

        return render(request, self.template_name, context)
    
    def post(self, request):
        profile = Profile.objects.filter(user=request.user).first()
        friends = Profile.objects.filter(user__in=profile.friends.all())

        context = {
            'form': self.search_form,
            'page': 'chat',
            'friends': friends,
        }
        return render(request, self.template_name, context)
    
    

class PersonalChatView(FormView):
    
    template_name = 'personal.html'

    search_form = SearchPeopleForm
    form_class = MessageForm
    
    def dispatch(self, request, *args, **kwargs):

        group_pk = self.kwargs['group_pk']

        chat_group = ChatGroup.objects.get(pk = group_pk)

        if Profile.objects.get(user=request.user) not in chat_group.members.all():
            return HttpResponseForbidden('<h1>У Вас немає доступу до цього чату</h1>')

        for message in ChatMessage.objects.filter(chat_group = chat_group):
            if Profile.objects.get(user=request.user) != message.author:
                message.view_by_users.add(Profile.objects.get(user=request.user))

            message.save()

        return super().dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        '''
        Метод відповідаючий за формування context
        '''
        # отримуємо context
        context =  super().get_context_data(**kwargs) 
        # отримуємо pk групи з динамічної URL
        group_pk = self.kwargs['group_pk']

        profile = Profile.objects.filter(user=self.request.user).first()
        groups = ChatGroup.objects.filter(members=profile)

        last_messages_subquery = ChatMessage.objects.filter(
            chat_group=OuterRef('pk')
        ).order_by('-sent_at')


        groups = groups.annotate(
            last_message=Subquery(last_messages_subquery.values('content')[:1]),
            last_message_time=Subquery(last_messages_subquery.values('sent_at')[:1])
        )

        friends = Profile.objects.filter(user__in=profile.friends.all())
        # отримуємо групу по pk
        context['chat_group'] = ChatGroup.objects.get(pk = group_pk) 
        context['user'] = Profile.objects.get(user=self.request.user)
        context['search_form'] = self.search_form
        context['groups'] = groups
        context['friends'] = friends
        context['page'] = 'chat'
        print(Profile.objects.get(user=self.request.user))
        # отримуємо історію усіх повідомлень цієї групи
        context['message_history'] = ChatMessage.objects.filter(chat_group_id = group_pk)
        return context
    
    def get_success_url(self):
        return reverse_lazy('group', kwargs={'group_pk': self.kwargs['group_pk']})


class GroupChatView(FormView):
    
    template_name = 'group.html'

    search_form = SearchPeopleForm
    form_class = MessageForm
    
    def dispatch(self, request, *args, **kwargs):

        group_pk = self.kwargs['group_pk']

        chat_group = ChatGroup.objects.get(pk = group_pk)

        if Profile.objects.get(user=request.user) not in chat_group.members.all():
            return HttpResponseForbidden('<h1>У Вас немає доступу до цього чату</h1>')

        for message in ChatMessage.objects.filter(chat_group = chat_group):
            if Profile.objects.get(user=request.user) != message.author:
                message.view_by_users.add(Profile.objects.get(user=request.user))

            message.save()

        return super().dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        '''
        Метод відповідаючий за формування context
        '''
        # отримуємо context
        context =  super().get_context_data(**kwargs) 
        # отримуємо pk групи з динамічної URL
        group_pk = self.kwargs['group_pk']

        profile = Profile.objects.filter(user=self.request.user).first()
        groups = ChatGroup.objects.filter(members=profile)

        last_messages_subquery = ChatMessage.objects.filter(
            chat_group=OuterRef('pk')
        ).order_by('-sent_at')


        groups = groups.annotate(
            last_message=Subquery(last_messages_subquery.values('content')[:1]),
            last_message_time=Subquery(last_messages_subquery.values('sent_at')[:1])
        )

        friends = Profile.objects.filter(user__in=profile.friends.all())
        # отримуємо групу по pk
        context['chat_group'] = ChatGroup.objects.get(pk = group_pk) 
        context['user'] = Profile.objects.get(user=self.request.user)
        context['search_form'] = self.search_form
        context['groups'] = groups
        context['friends'] = friends
        context['page'] = 'chat'
        print(Profile.objects.get(user=self.request.user))
        # отримуємо історію усіх повідомлень цієї групи
        context['message_history'] = ChatMessage.objects.filter(chat_group_id = group_pk)
        return context
    
    def get_success_url(self):
        return reverse_lazy('group', kwargs={'group_pk': self.kwargs['group_pk']})
    

def redirect_to_personal_chat(request, user1_pk, user2_pk):
    user1 = Profile.objects.get(pk = user1_pk)
    user2 = Profile.objects.get(pk = user2_pk)

    #chat : PersonalChat = PersonalChat.objects.filter(is_personal_chat = True).filter(members = user1).filter(members = user2).first()
    chat : ChatGroup = ChatGroup.objects.filter(is_personal_chat = True).filter(members = user1).filter(members = user2).first()

    if not chat:
        #chat = PersonalChat.objects.create(name = f"Chat {user1} and {user2}", is_personal_chat = True)
        chat = ChatGroup.objects.create(name = f"Chat {user1} and {user2}", is_personal_chat = True)
        chat.members.add(user1, user2)
        chat.save()

    return redirect('personal', chat.pk)