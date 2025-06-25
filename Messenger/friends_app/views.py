from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.urls import reverse
from .models import FriendRequest
from reg.models import Profile

class FriendsView(TemplateView):
    template_name = 'friends_app/friends.html'

    def post(self, request, *args, **kwargs):
        profile = Profile.objects.get(user=request.user)
        print(profile)
        action = request.POST.get('action')
        user_id = request.POST.get('user_id')

        if action == 'accept_request' and user_id:
            try:
                friend_request = FriendRequest.objects.get(id=user_id, to_who=profile)
                from_profile = friend_request.from_who
        
                if from_profile != profile:
                    profile.friends.add(from_profile.user)
                    from_profile.friends.add(profile.user)
        
                friend_request.delete()

            except Profile.DoesNotExist:
                pass

        return redirect('friends')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = 'friends'

        profile = Profile.objects.get(user=self.request.user)

        friend_requests_qs = FriendRequest.objects.filter(to_who=profile)

        context['friend_requests'] = [
            {
                'id': fr.id,
                'name': fr.from_who.user.get_full_name() or fr.from_who.user.username,
                'username': fr.from_who.user.username,
                'avatar_url': (
                    fr.from_who.image.url
                    if fr.from_who.image and hasattr(fr.from_who.image, 'url')
                    else self.request.build_absolute_uri('/static/home_app/img/Avatar.png')
                )
            }
            for fr in friend_requests_qs
        ]

        friends_ids = profile.friends.values_list('id', flat=True)
        sent_ids = friend_requests_qs.values_list('from_who_id', flat=True)

        recommendations_qs = Profile.objects.exclude(id__in=list(friends_ids) + list(sent_ids) + [profile.id])[:6]

        context['recommendations'] = [
            {
                'id': p.id,
                'name': p.user.get_full_name() or p.user.username,
                'username': p.user.username,
                'avatar_url': p.image.url if p.image and hasattr(p.image, 'url') else self.request.build_absolute_uri('/static/img/Avatar.png')
            }
            for p in recommendations_qs
        ]

        friends_qs = profile.friends.all()[:6]
        context['all_friends'] = []

        for user in friends_qs:
            try:
                prof = Profile.objects.get(user=user)
                avatar_url = prof.image.url if prof.image and hasattr(prof.image, 'url') else self.request.build_absolute_uri('/static/img/Avatar.png')
                context['all_friends'].append({
                    'id': prof.id,
                    'name': user.get_full_name() or user.username,
                    'username': user.username,
                    'avatar_url': avatar_url,
                })
            except Profile.DoesNotExist:
                continue

        return context