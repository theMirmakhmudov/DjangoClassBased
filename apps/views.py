from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DeleteView
from .models import People


class Home(TemplateView):
    template_name = "home.html"


class UsersList(ListView):
    model = People
    context_object_name = 'users'
    template_name = 'user_list.html'


class UsersDelete(DeleteView):
    model = People
    context_object_name = 'users'
    pk_url_kwarg = 'pk'
    success_url = '/'
    template_name = 'user_list.html'

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
