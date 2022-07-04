from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('blog/', views.index, name="index"),
    path('<str:slug>', views.blog_detailView, name = 'blog_detail'), #so that the slug of a particular post is attached to the end of the url e.g blog/(slug-name)
   
]


