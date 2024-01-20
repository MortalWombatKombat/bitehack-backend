from django.urls import include, path
from rest_framework import routers

from bitehack2024.accounts.views import AddictionViewSet, MoodEntryViewSet

app_name = "accounts"

urlpatterns = [
    path(r"", include("djoser.urls")),
    path(r"", include("djoser.urls.jwt")),
]

router = routers.DefaultRouter()

router.register(r"addictions", AddictionViewSet, "addictions")
router.register(r"mood_entry", MoodEntryViewSet, "mood_entry_create")

urlpatterns += router.urls
