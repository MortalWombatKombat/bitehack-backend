from django.db import models

from bitehack2024.challenges.models import (
    Educational,
    QuestionSet,
    SocraticDialogueQuestions,
    TimeEvent,
)
from bitehack2024.challenges.serializers import (
    EducationalSerializer,
    QuestionSetSerializer,
    SocraticDialogueQuestionsSerializer,
    TimeEventSerializer,
)


class ChallengeTypes(models.TextChoices):
    SOCRATIC_DIALOGUE = "socratic_dialogue", "Socratic dialogue"
    QuestionSet = "question_set", "Question set"
    EDUCATIONAL = "educational", "Educational"
    TIME_EVENT = "time_event", "Time event"


CHALLENGE_MODEL_TYPE_MAP = {
    SocraticDialogueQuestions: ChallengeTypes.SOCRATIC_DIALOGUE,
    QuestionSet: ChallengeTypes.QuestionSet,
    Educational: ChallengeTypes.EDUCATIONAL,
    TimeEvent: ChallengeTypes.TIME_EVENT,
}

CHALLENGE_TYPE_SERIALIZER_MAP = {
    ChallengeTypes.SOCRATIC_DIALOGUE: SocraticDialogueQuestionsSerializer,
    ChallengeTypes.QuestionSet: QuestionSetSerializer,
    ChallengeTypes.EDUCATIONAL: EducationalSerializer,
    ChallengeTypes.TIME_EVENT: TimeEventSerializer,
}
