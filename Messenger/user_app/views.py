from django.views.generic import DetailView
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from my_publications.models import User_Post
from reg.models import Profile


class ProfileView(DetailView):
    model = Profile
    template_name = 'user.html'
    context_object_name = 'profile'

    def get_object(self):
        id = self.kwargs.get('id')
        return get_object_or_404(Profile, id=id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = self.get_object()

        user_posts = User_Post.objects.filter(user=profile).order_by('-id')

        context['page'] = 'home'
        context['posts'] = user_posts

        if profile:
            posts_count = profile.posts.count()
            context['posts_count'] = posts_count

            followers_count = profile.followers.count()
            context['followers_count'] = followers_count

            friends_count = profile.friends.count()
            context['friends_count'] = friends_count
        else:
            context['posts_count'] = 0
            context['followers_count'] = 0
            context['friends_count'] = 0


        return context