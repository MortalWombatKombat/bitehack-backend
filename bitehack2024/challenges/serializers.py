from rest_framework import serializers

from bitehack2024.challenges.models import (
    Educational,
    QuestionSet,
    SocraticDialogueQuestions,
    TimeEvent,
)


class QuestionSetSerializer(serializers.ModelSerializer):
    questions = serializers.SerializerMethodField()

    class Meta:
        model = QuestionSet
        fields = "__all__"

    def get_questions(self, obj):
        return obj.questions.values_list("value", flat=True)


class EducationalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Educational
        fields = "__all__"


class TimeEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeEvent
        fields = "__all__"


class SocraticDialogueQuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocraticDialogueQuestions
        fields = "__all__"
