from django.contrib import admin
from django.contrib.postgres.fields import ArrayField
from django.db import models


class Question(models.Model):
    title = models.CharField(max_length=255)
    value = models.TextField()

    def __str__(self):
        return f"{self.title} - {self.value}"


class QuestionSet(models.Model):
    title = models.CharField(max_length=255)
    questions = models.ManyToManyField(Question)

    def __str__(self):
        return self.title


class Educational(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    ref = ArrayField(
        models.URLField(),
        size=10,
        blank=True,
    )

    def __str__(self):
        return self.title


class TimeEvent(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    time_sec = models.IntegerField()

    def __str__(self):
        return self.title


class SocraticDialogueQuestions(models.Model):
    title = models.CharField(max_length=255)
    Value = models.TextField()

    def __str__(self):
        return self.title
