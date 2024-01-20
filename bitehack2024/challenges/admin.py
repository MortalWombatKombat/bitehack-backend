from django.contrib import admin

from bitehack2024.challenges.models import (
    Educational,
    Question,
    QuestionSet,
    SocraticDialogueQuestions,
    TimeEvent,
)


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    pass


@admin.register(QuestionSet)
class QuestionSetAdmin(admin.ModelAdmin):
    pass


@admin.register(Educational)
class EducationalAdmin(admin.ModelAdmin):
    pass


@admin.register(SocraticDialogueQuestions)
class SocraticDialogueQuestionsAdmin(admin.ModelAdmin):
    pass


@admin.register(TimeEvent)
class TimeEventAdmin(admin.ModelAdmin):
    pass
