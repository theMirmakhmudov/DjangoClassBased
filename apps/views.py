from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DeleteView, UpdateView
from .models import People
from .forms import PeopleForm


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


class UsersUpdateView(UpdateView):
    model = People
    template_name = 'people_form.html'
    context_object_name = 'user'
    pk_url_kwarg = 'pk'
    success_url = '/'
    form_class = PeopleForm
