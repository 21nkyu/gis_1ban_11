"""ik_1ban_11 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from articleapp.views import ArticleListView

urlpatterns = [
    path('', ArticleListView.as_view(), name='home'),

    path('admin/', admin.site.urls),
    path('accounts/', include('accountapp.urls')),
    path('profiles/', include('profileapp.urls')), #http 12903810293/profile/urls
    path('articles/', include('articleapp.urls')),
    path('comments/', include('commentapp.urls')),
    path('projects/', include('projectapp.urls')),#프로젝트 앱의 url.py에서 분기

    path('subscribe/', include('subscribeapp.urls')),
    path('like/', include('likeapp.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  #파일경로 이기 때문에 별도로 설정 개발환경에서 미디어를 이용할 수 있음