from django.db.models.signals import post_save
from django.dispatch import receiver

from psb_learning.projects.models import Project

from .models import Quizz


@receiver(post_save, sender=Project)
def generate_questions(instance: Project, created: bool, **kwargs) -> None:
    """Создаёт викторину и генерирует для неё вопросы"""
    if created:
        # Создаём викторину
        quizz_name = f'Вводная викторина по проекту "{instance.name}"'
        quizz: Quizz = Quizz.objects.create(
            project=instance,
            name=quizz_name
        )

        quizz.generate_questions_and_options()
