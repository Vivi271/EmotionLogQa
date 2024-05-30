from django.urls import path
from EmotionTracker.views import home_view, emotion_entry_view, progress_view, chatbot_view
from EmotionTracker.views_streaming import video_feed, get_html

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('EmotionLog/RegEmocion/', emotion_entry_view, name='emotion_entry'),
    path('EmotionLog/ValidacionProgreso/', progress_view, name='progress'),
    path('EmotionLog/Chatbot/', chatbot_view, name='chatbot'),
    path('video', video_feed, name='video_feed'),
    path('streaming', get_html, name='streaming_home'),
]
