"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include
from blog import views
from blog.feeds import PostsRssFeed

app_name = 'blog'

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('post/<int:pk>', views.PostDetailView.as_view(), name='detail'),
    path('archives/<int:year>/<int:month>', views.ArchivesView.as_view(), name='archives'),
    path('tag/<int:pk>', views.TagView.as_view(), name='tag'),
    path('category/<int:pk>', views.CategoryView.as_view(), name='category'),
    path('rss', PostsRssFeed(), name='rss'),
]
