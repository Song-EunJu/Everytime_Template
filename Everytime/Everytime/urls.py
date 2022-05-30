"""Everytime URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from EverytimeApp import views as everytime
from accounts import views as accounts
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', everytime.landing, name='landing'),
    path('main/',everytime.main, name='main'),
    path('freeBoard/', everytime.free, name='free'),
    path('freeBoard/<int:post_id>/', everytime.detail, name='detail'),
    # 숫자형으로 url이 설계되는데, post pk에 해당하는 애들은 post_id 라는 이름으로써 
    # detail 함수에 넘겨줄거야!!!

    path('freeBoard/<int:post_id>/update/', everytime.update, name='update'),
    path('freeBoard/<int:post_id>/delete/', everytime.delete, name='delete'),
    
    path('graduateBoard/', everytime.graduate, name='graduate'),
    path('auth/', include('accounts.urls')),
    path('create/', everytime.create, name='create'), # 글 생성하기
    # path('search/', everytime.search, name='search'), # 검색하기

    path('createComment/<int:post_id>/', everytime.createComment, name='createComment'),
    path('createComment/<int:post_id>/<int:comment_id>', everytime.createReply, name='createReply')
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)



# media 파일에 접근할 수 있는 url도 추가해줘야 함
