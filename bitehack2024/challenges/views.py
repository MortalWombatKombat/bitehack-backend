import random

from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from bitehack2024.accounts.models import Addiction
from bitehack2024.challenges.constants import (
    CHALLENGE_MODEL_TYPE_MAP,
    CHALLENGE_TYPE_SERIALIZER_MAP,
)


class ChallengeViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self, challenge_type):
        return CHALLENGE_TYPE_SERIALIZER_MAP.get(challenge_type)

    @action(detail=False, methods=["get"])
    def draw(self, request):
        user = request.user

        if user.addiction is None:
            user.addiction = Addiction.objects.get_or_create(name="Other")[0]

        challenges = (
            list(user.addiction.question_sets.all())
            + list(user.addiction.educational.all())
            + list(user.addiction.time_events.all())
            + list(user.addiction.socratic_dialogue_questions.all())
        )

        if not challenges:
            return Response(status=status.HTTP_204_NO_CONTENT)

        challenge = random.choice(challenges)
        challenge_type = CHALLENGE_MODEL_TYPE_MAP.get(type(challenge))

        serializer_class = self.get_serializer_class(challenge_type)
        serializer = serializer_class(challenge)

        return Response(
            {
                "type": challenge_type,
                "data": serializer.data,
            }
        )

    @action(detail=False, methods=["post"])
    def finish_challenge(self, request):
        user = request.user
        user.challenges_done += 1
        user.save()
        return Response(status=status.HTTP_200_OK)
