from django.urls import path
from .views import gallery_video, gallery_photo

app_name = "gallery"
urlpatterns = [
    path('video/', gallery_video, name="video"),
    path('video/?page=<page_number>', gallery_video, name="video"),
    path('<slug>/', gallery_photo, name="photo"),
    path('<slug>/?page=<page_number>', gallery_photo, name="photo"),
]
