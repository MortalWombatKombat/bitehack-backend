from djoser.views import UserViewSet
from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ReadOnlyModelViewSet

from bitehack2024.accounts.models import Addiction, MoodEntry
from bitehack2024.accounts.serializers import AddictionSerializer, MoodEntrySerializer


class CustomUserViewSet(UserViewSet):
    pass


class AddictionViewSet(ReadOnlyModelViewSet):
    model = Addiction
    serializer_class = AddictionSerializer


class MoodEntryViewSet(mixins.CreateModelMixin, GenericViewSet):
    model = MoodEntry
    serializer_class = MoodEntrySerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return (
            MoodEntry.objects.filter(user=self.request.user).order_by("-date").first()
        )

    @action(detail=False, methods=["get"])
    def current_mood(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
