from django.urls import path
from .views import UsersList, UsersDelete

urlpatterns = [
    path('', UsersList.as_view(), name="home"),
    path('delete/<int:pk>', UsersDelete.as_view(), name='delete'),
]
