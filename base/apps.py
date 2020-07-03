from django.apps import AppConfig
from constance.apps import ConstanceConfig


class BaseConfig(AppConfig):
    name = 'base'
    verbose_name = "Главная страница"


class CustomConstance(ConstanceConfig):
    verbose_name = "Контактные данные"
