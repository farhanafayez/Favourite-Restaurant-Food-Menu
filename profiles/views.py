from django.shortcuts import render, get_object_or_404
from djnago.http import Http404
from djnago.views.generic import DetailView
from django.contrib.auth import get_user_model
# Create your views here.

User = get_user_model()
class ProfileDetailView(DetailView):
    queryet = User.objects.filter(is_active = True)
    template_name='profiles/user.html'

    def get_object(self):
        username = self.kwargs.get("username")
        if username is None:
            raise Http404
        return get_object_or_404(User, username_iexact=username, is_active=True)