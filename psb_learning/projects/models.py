from django.db import models


class Project(models.Model):
    """Модель проекта"""

    name = models.CharField(
        max_length=512,
        verbose_name="название"
    )

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        verbose_name = "проект"
        verbose_name_plural = "проекты"
