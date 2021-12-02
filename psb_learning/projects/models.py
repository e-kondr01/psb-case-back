from django.db import models


class Project(models.Model):
    """Модель проекта"""

    name = models.CharField(
        max_length=512,
        verbose_name="название"
    )

    goals = models.TextField(
        blank=True,
        verbose_name="цели и задачи"
    )

    project_type = models.CharField(
        max_length=512,
        blank=True,
        verbose_name="тип проекта"
    )

    events = models.TextField(
        blank=True,
        verbose_name="обязательные мероприятия"
    )

    stages = models.TextField(
        blank=True,
        verbose_name="план работы и контрольные точки"
    )

    results = models.TextField(
        blank=True,
        verbose_name="результаты проекта"
    )

    technologies = models.TextField(
        blank=True,
        verbose_name="стек технологий"
    )

    more_info = models.TextField(
        blank=True,
        verbose_name="дополнительная информация"
    )

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        verbose_name = "проект"
        verbose_name_plural = "проекты"


class ProjectLink(models.Model):
    """Модель ссылки на инструмент проекта"""

    name = models.CharField(
        max_length=512,
        verbose_name="название"
    )

    link = models.URLField(
        verbose_name="ссылка"
    )

    project = models.ForeignKey(
        to=Project,
        on_delete=models.CASCADE,
        related_name="links",
        verbose_name="проект"
    )

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        verbose_name = "ссылка проекта"
        verbose_name_plural = "ссылки проектов"


class ProjectFile(models.Model):
    """Модель файла к проекту"""

    project = models.ForeignKey(
        to=Project,
        on_delete=models.CASCADE,
        related_name="files",
        verbose_name="проект"
    )

    file = models.FileField(
        verbose_name="файл"
    )

    def __str__(self) -> str:
        return f"{self.file}"

    class Meta:
        verbose_name = "файл проекта"
        verbose_name_plural = "файлы проектов"


class ProjectMember(models.Model):
    """Модель участника проекта"""

    name = models.CharField(
        max_length=512,
        verbose_name="ФИО"
    )

    role = models.CharField(
        max_length=512,
        verbose_name="должность"
    )

    photo = models.ImageField(
        verbose_name="фотография",
        blank=True,
        null=True
    )

    project = models.ForeignKey(
        to=Project,
        on_delete=models.CASCADE,
        related_name="members",
        verbose_name="проект"
    )

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        verbose_name = "участник проекта"
        verbose_name_plural = "участники проектов"
