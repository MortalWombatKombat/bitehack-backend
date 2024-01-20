from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to="avatars/", null=True, blank=True)
    addiction = models.ForeignKey(
        "Addiction", on_delete=models.PROTECT, null=True, blank=True
    )
    challenges_done = models.IntegerField(default=0)

    def __str__(self):
        return self.username


class Addiction(models.Model):
    name = models.CharField(max_length=255)
    time_events = models.ManyToManyField("challenges.TimeEvent", blank=True)
    educational = models.ManyToManyField("challenges.Educational", blank=True)
    question_sets = models.ManyToManyField("challenges.QuestionSet", blank=True)
    socratic_dialogue_questions = models.ManyToManyField(
        "challenges.SocraticDialogueQuestions", blank=True
    )

    def __str__(self):
        return self.name


class MoodEntry(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    current_mood_value = models.IntegerField(
        validators=[MaxValueValidator(100), MinValueValidator(0)]
    )
    addiction_manage_progress = models.IntegerField(
        validators=[MaxValueValidator(100), MinValueValidator(0)]
    )

    def __str__(self):
        return f"{self.user}: {self.date}"
