from typing import Optional

from django.contrib.auth import get_user_model
from django.db import models


class Quizz(models.Model):
    """Модель викторины"""

    name = models.CharField(
        max_length=512,
        verbose_name="название"
    )

    def get_next_question(self, order: int) -> Optional[int]:
        """Возвращает id следующего вопроса в викторине"""
        if self.questions.filter(order=order+1):
            return self.questions.filter(order=order+1).first().pk
        else:
            return None

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        verbose_name = "викторина"
        verbose_name_plural = "викторины"


class Question(models.Model):
    """Модель вопроса в викторине"""

    text = models.CharField(
        max_length=512,
        verbose_name="содержание вопроса"
    )

    quizz: Quizz = models.ForeignKey(
        to=Quizz,
        on_delete=models.CASCADE,
        related_name="questions",
        verbose_name="викторина"
    )

    correct_info = models.TextField(
        blank=True,
        verbose_name="информация при правильном ответе"
    )

    incorrect_info = models.TextField(
        blank=True,
        verbose_name="информация при неправильном ответе"
    )

    order = models.SmallIntegerField(
        null=True,
        blank=True,
        verbose_name="порядок"
    )

    rating_change = models.SmallIntegerField(
        default=5,
        verbose_name="рейтинг за вопрос"
    )

    def check_answer(self, answer: "Option", user: get_user_model()) -> bool:
        """Проверяет правильность ответа.
        При правильном ответе увеличивает рейтинг пользователя"""
        if answer.question == self and answer.is_correct:
            user.increase_rating(self.rating_change)
            return True
        else:
            return False

    def get_info(self, correct: bool) -> str:
        """Возвращает информацию в зависимости от выбранного ответа"""
        return self.correct_info if correct else self.incorrect_info

    def get_rating_change(self, correct: bool) -> str:
        """Возвращает изменение рейтинга в зависимости от выбранного ответа"""
        return f"+{self.rating_change}" if correct else "0"

    def __str__(self) -> str:
        return f"{self.text}"

    class Meta:
        verbose_name = "вопрос"
        verbose_name_plural = "вопросы"


class Option(models.Model):
    """Модель варианта ответа на вопрос в викторине"""

    text = models.CharField(
        max_length=512,
        verbose_name="содержание вопроса"
    )

    question = models.ForeignKey(
        to=Question,
        on_delete=models.CASCADE,
        related_name="options",
        verbose_name="вопрос"
    )

    is_correct = models.BooleanField(
        default=False,
        verbose_name="правильный вариант?"
    )

    def __str__(self) -> str:
        return f"{self.text}"

    class Meta:
        verbose_name = "вариант ответа"
        verbose_name_plural = "варианты ответа"
