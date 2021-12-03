import random
from typing import Optional

from django.contrib.auth import get_user_model
from django.db import models

from psb_learning.projects.models import Project


class Quizz(models.Model):
    """Модель викторины"""

    project: Project = models.ForeignKey(
        to=Project,
        on_delete=models.CASCADE,
        related_name="quizzes",
        blank=True,
        null=True,
        verbose_name="проект"
    )

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

    def get_next_question_order(self) -> int:
        """Возвращает, какой порядок должен быть у следующего вопроса"""
        if self.questions.exists():
            last_order = self.questions.order_by("-order").first().order
            return last_order + 1
        else:
            return 1

    def get_option_texts(self, project_attribute_name: str) -> list[str]:
        """Возвращает список уникальных значений атрибута у других проектов"""

        option_texts = list(
            Project.objects.values_list(
                project_attribute_name,
                flat=True
            ).distinct()
        )

        # Удаляем текст правильной опции
        right_option_text = getattr(self.project, project_attribute_name)
        option_texts.remove(right_option_text)

        # Выбрать из них не более 3 случайных
        if len(option_texts) > 3:
            return random.sample(option_texts, 3)
        else:
            return option_texts

    def generate_questions_and_options(self) -> None:
        """Генерирует для викторины вопросы и варианты ответа
        по различным атрибутам проекта"""

        attributes_and_question_texts = {
            "goals": "Какая из перечисленных ниже задач относится к твоему проекту?",
            "project_type": "Какая методология используется в твоём проекте?",
            "technologies": "Какой технологический стек твоего проекта?",
            "events": "Какие обязательные мероприятия есть в твоём проекте?"
        }

        for attribute, question_text in attributes_and_question_texts.items():
            self.generate_question_and_options(attribute, question_text)

    def generate_question_and_options(self,
                                      project_attribute_name: str,
                                      question_text: str
                                      ) -> None:
        """Создаёт вопрос и варианты ответа с данным текстом по
        данному атрибуту проекта, исходя из значений этого
        атрибута в других проектах"""
        try:
            if getattr(self.project, project_attribute_name):
                right_option_text = getattr(self.project, project_attribute_name)

                # Создаём вопрос
                question = Question.objects.create(
                    quizz=self,
                    text=question_text,
                    order=self.get_next_question_order()
                )

                # Получаем уникальные значения атрибута с других проектов
                option_texts = self.get_option_texts(project_attribute_name)

                # Создаём варианты ответа
                Option.objects.create(
                    question=question,
                    text=right_option_text,
                    is_correct=True
                )
                for text in option_texts:
                    Option.objects.create(
                        question=question,
                        text=text,
                        is_correct=False
                    )
                return None
            else:
                # Поле не заполнено у текущего проекта
                return None
        except AttributeError:
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
