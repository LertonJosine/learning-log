

# from django import views
# from django.conf.urls import url
from pathlib import Path
from django.contrib import admin
from django.urls import path
from learning_logs.views import home, topics, topic, new_topic, new_entry, edit_entry
from users.views import registrar

urlpatterns = [
    path('', home, name='index'),
    path('register/', registrar, name='register' ),
    path('topics/', topics, name='topics'),
    path('topic/<int:topic_id>/',topic, name='topic'),
    path('new_topic/', new_topic, name='new_topic'),
    path('new_entry/<int:topic_id>/', new_entry, name='new_entry'),
    path('edit_entry/<int:entry_id>/', edit_entry, name='edit_entry'),
    
    
]
