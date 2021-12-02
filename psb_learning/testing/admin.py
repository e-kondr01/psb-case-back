from django.contrib import admin

from psb_learning.testing.models import Answer, Question, Quizz

admin.site.register(Quizz)
admin.site.register(Question)
admin.site.register(Answer)
