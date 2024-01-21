from rest_framework import serializers

from bitehack2024.accounts.models import Addiction, CustomUser, MoodEntry


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "avatar",
            "addiction",
            "challenges_done",
        ]


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
