"""FinEmotionLog URL Configuration"""

from django.contrib import admin
from django.urls import path
from EmotionTracker.views import home_view, emotion_entry_view, progress_view, chatbot_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('EmotionLog/RegEmocion/', emotion_entry_view, name='emotion_entry'),
    path('EmotionLog/ValidacionProgreso/', progress_view, name='progress'),
    path('EmotionLog/Chatbot/', chatbot_view, name='chatbot'),
]
