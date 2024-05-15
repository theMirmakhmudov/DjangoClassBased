from django.urls import path
from .views import UsersList, UsersDelete, UsersUpdateView

urlpatterns = [
    path('', UsersList.as_view(), name="home"),
    path('delete/<int:pk>', UsersDelete.as_view(), name='delete'),
    path('update/<int:pk>', UsersUpdateView.as_view(), name='update'),
]
