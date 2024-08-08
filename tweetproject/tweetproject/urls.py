from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from tweet.views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('tweetlist/', tweet_list, name='tweet_list'),
    path('tweetcreate/', tweet_create, name='tweet_create'),
    path('<int:tweet_id>/edit/', tweet_edit, name='tweet_edit'),
    path('<int:tweet_id>/delete/', tweet_delete, name='tweet_delete'),
    path('tweet/', include('tweet.urls')),
    path('register/', register, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
