# wwwapp/blog/urls.py

from django.urls import path

from blog.views import test, homepage, post_show

urlpatterns = [
    path('', homepage),
    path('test/<imie>/<int:wiek>', test),
    path('post/<slug>', post_show, name='post_show')
]

