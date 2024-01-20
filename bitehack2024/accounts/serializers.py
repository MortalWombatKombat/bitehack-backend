from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated

from bitehack2024.accounts.models import Addiction, CustomUser, MoodEntry


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = (
            "id",
            "username",
        )


class AddictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Addiction
        fields = ["id", "name"]


class MoodEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = MoodEntry
        fields = [
            "current_mood_value",
            "addiction_manage_progress",
        ]

    def create(self, validated_data):
        validated_data["user"] = self.context["request"].user

        return MoodEntry.objects.create(**validated_data)
