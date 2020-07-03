from django.urls import path
from .views import blog, post

app_name = "blog"
urlpatterns = [
    path('', blog, name="home"),
    path('<slug>/', post, name="post"),
]
