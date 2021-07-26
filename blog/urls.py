"""CoderLife URL Configuration

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
from django.urls import path
from . import views


app_name = 'blog'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('<slug:post_name>/', views.post_detail, name = 'post_detail'),
    path('<slug:slug>/comment_<comment_id>_reply/', views.reply_page, name='reply'),
    path('tag/<slug:tag_slug>/', views.index, name='post_tag')
]

