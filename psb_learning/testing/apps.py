from django.apps import AppConfig


class TestingAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "psb_learning.testing"
    verbose_name = "Тестирование"