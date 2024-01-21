from datetime import timedelta

from django.utils import timezone
from djoser.views import UserViewSet
from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ReadOnlyModelViewSet

from bitehack2024.accounts.models import Addiction, CustomUser, MoodEntry
from bitehack2024.accounts.serializers import AddictionSerializer, MoodEntrySerializer


class CustomUserViewSet(UserViewSet):
    queryset = CustomUser.objects.all()


class AddictionViewSet(ReadOnlyModelViewSet):
    queryset = Addiction.objects.all()
    serializer_class = AddictionSerializer


class MoodEntryViewSet(mixins.CreateModelMixin, GenericViewSet):
    model = MoodEntry
    serializer_class = MoodEntrySerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        past_threshold = timezone.now() - timedelta(hours=12)
        return (
            MoodEntry.objects.filter(user=self.request.user, date__gt=past_threshold)
            .order_by("-date")
            .first()
        )

    @action(detail=False, methods=["get"])
    def current_mood(self, request, *args, **kwargs):
        instance = self.get_object()

        if instance is None:
            return Response()

        serializer = self.get_serializer(instance)
        return Response(serializer.data)
