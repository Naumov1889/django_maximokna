from django.urls import path
from .views import record_callback, callback_page

app_name = "callback"
urlpatterns = [
    path('record_callback/', record_callback, name="home"),
    path('', callback_page, name="page")
]
