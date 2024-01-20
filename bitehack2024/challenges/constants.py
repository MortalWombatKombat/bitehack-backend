from django.db import models

from bitehack2024.challenges.models import (
    Educational,
    QuestionSet,
    SocraticDialogueQuestions,
    TimeEvent,
)


class ChallengeTypes(models.TextChoices):
    SOCRATIC_DIALOGUE = "socratic_dialogue", "Socratic dialogue"
    QuestionSet = "question_set", "Question set"
    EDUCATIONAL = "educational", "Educational"
    TIME_EVENT = "time_event", "Time event"


CHALLENGE_TYPE_MODEL_MAP = {
    ChallengeTypes.SOCRATIC_DIALOGUE: SocraticDialogueQuestions,
    ChallengeTypes.QuestionSet: QuestionSet,
    ChallengeTypes.EDUCATIONAL: Educational,
    ChallengeTypes.TIME_EVENT: TimeEvent,
}
