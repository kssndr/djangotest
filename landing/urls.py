from django.urls import path
from . import views
# from django.conf.urls import patterns
from landing.views import ItemList


# urlpatterns = [
#     path('', views.item_list, name='item_list'),
# ]

urlpatterns = [
    path('', ItemList.as_view()),
]
