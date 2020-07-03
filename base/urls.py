from django.urls import path
from .views import home, policy_page, plastikovye_okna

app_name = "base"
urlpatterns = [
    path('', home, name="home"),
    path('policy/', policy_page, name="policy_page"),
    path('plastikovye-okna/', plastikovye_okna, name="plastikovye_okna"),
]
