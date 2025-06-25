from django.shortcuts import render, redirect
from django.views.generic import ListView
from my_publications.models import User_Post, PostImage
from reg.models import Profile


class CreatePublicationView(ListView):
    model = User_Post
    template_name = "my_publications/create.html"
    context_object_name = 'posts'

    def post(self, request, *args, **kwargs):
        title = request.POST.get('title')
        topic = request.POST.get('topic')
        description = request.POST.get('description')
        link = request.POST.get('link')
        images = request.FILES.getlist('img')

        if title and topic and description:
            profile, _ = Profile.objects.get_or_create(user=request.user)

            post = User_Post.objects.create(
                title=title,
                topic=topic,
                description=description,
                link=link,
                user = profile
            )

            for img_file in images[:3]:
                PostImage.objects.create(post=post, image=img_file)

        elif any(k.startswith("del-") for k in request.POST):
            for k in request.POST:
                if k.startswith("del-"):
                    post_id = k.split("-")[1]
                    User_Post.objects.filter(pk=post_id).delete()
                    break
                
        return redirect('create') 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page"] = 'create'
        context["show_modal"] = False

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