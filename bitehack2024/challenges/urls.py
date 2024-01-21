from rest_framework import routers

from bitehack2024.challenges.views import ChallengeViewSet

router = routers.DefaultRouter()
router.register(r"challenges", ChallengeViewSet, "challenges")

urlpatterns = router.urls
