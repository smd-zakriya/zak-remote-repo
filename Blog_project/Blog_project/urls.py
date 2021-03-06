"""Blog_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.PostList),
    path('tag/<slug:tag_slug>', views.PostList, name='post_list_with_tag'),
    #path('', views.PostListView.as_view()),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>', views.Detail_Post_view, name='post_details'),
    path('share-post/<int:pk>', views.send_mail_view),
    path('search/', views.search_view, name='search_post'),
    path('about/', views.about_view),
    path('contact/', views.contact_view),

]
