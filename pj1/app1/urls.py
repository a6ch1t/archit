from django.urls import path
from app1  import views
urlpatterns= [
    path('messages/', views.MessageListView.as_view(), name='message-list'),
    path('messages/create/', views.MessageCreativeView.as_view(), name='message-create'),
]