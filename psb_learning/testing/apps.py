from django.apps import AppConfig


class TestingAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "psb_learning.testing"
    verbose_name = "Тестирование"

    def ready(self):
        # pylint: disable=import-outside-toplevel,unused-import
        from psb_learning.testing import signals
