from django.views.generic import ListView
from my_publications.models import User_Post
from django.contrib.auth.mixins import LoginRequiredMixin
from reg.models import Profile

class HomeView(LoginRequiredMixin, ListView):
    model = User_Post
    template_name = "home_app/home.html"
    context_object_name = 'posts'
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page"] = 'home'

        if self.request.session.get('has_just_joined') == True:
            context['modal'] = True
            self.request.session.pop('has_just_joined', None)

        profile = Profile.objects.filter(user=self.request.user).first()
        context['profile'] = profile

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