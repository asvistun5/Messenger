from django.views.generic import TemplateView
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.views import View
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from .forms import AlbumForm
from datetime import datetime
from reg.models import Profile

class SettingsView(TemplateView):
    template_name = 'settings_app/settings.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page"] = 'settings'

        profile = Profile.objects.filter(user=self.request.user).first()
        context['profile'] = profile


        if 'form' not in context:
            context['form'] = AlbumForm(instance=profile)

        return context

    def post(self, request, *args, **kwargs):
        profile = Profile.objects.filter(user=request.user).first()
        form = AlbumForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('settings')  
        
        
        context = self.get_context_data()
        context['form'] = form
        return self.render_to_response(context)

@login_required
def update_profile(request):

    profile = Profile.objects.filter(user=request.user).first()

    if request.method == 'POST':
        user = request.user
        profile = user.profile
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        if request.POST.get('password'):
            user.set_password(request.POST.get('password'))

        birth_date_str = request.POST.get('birth_date')
        if birth_date_str:
            try:
                birth_date = datetime.strptime(birth_date_str.strip('“”"'), '%Y-%m-%d').date()
                profile.birth_date = birth_date
            except ValueError:
                pass
        user.save()
        profile.save()
        return render(request, "settings_app/settings.html", {"page": "settings", 'profile': profile})
    
class AlbumsView(TemplateView):
    template_name = "settings_app/albums.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page"] = 'settings'
        context["form"] = AlbumForm()
        context["image"] = Profile.objects.get(user=self.request.user).image.url
        return context