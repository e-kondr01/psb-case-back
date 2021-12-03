from django.db import models


class Quizz(models.Model):
    """Модель викторины"""

    name = models.CharField(
        max_length=512,
        verbose_name="название"
    )

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

    quizz = models.ForeignKey(
        to=Quizz,
        on_delete=models.CASCADE,
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
