from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("",views.home,name = "home"),
    path("login",views.login, name = "login"),
    path("logout/",views.logout, name = "logout"),
    path("register/",views.register, name = "register"),
    path("add_blogs/",views.add_blogs, name = "add_blogs"),
    path("my_blogs/",views.my_blogs, name = "my_blogs"),
    path('blog_delete/<id>/' , views.blog_delete , name="blog_delete"),
    path('update_blog/<id>/' , views.update_blog , name="update_blog"),
    path("see_blogs/<id>/",views.see_blogs, name = "see_blogs"),
    path("my_profile/",views.my_profile, name = "my_profile"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
