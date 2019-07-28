from django.urls import path
from .views import index

urlpatterns = [
    path(r'index', index, name='polls_list'),

]
