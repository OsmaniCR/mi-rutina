from rest_framework.routers import DefaultRouter
from .views import (
    RoutineViewSet,
    RoutineDetailViewSet,
    ExerciseViewSet,
    UserRoutineViewSet,
    ExerciseListViewSet,
)

router = DefaultRouter()
router.register("routine-details", RoutineDetailViewSet, basename="routine-details")
router.register("exercises", ExerciseViewSet, basename="exercises")
router.register("my-routines", UserRoutineViewSet, basename="my-routines")
router.register("exercise-list", ExerciseListViewSet, basename="exercise-list")
router.register("", RoutineViewSet, basename="routines")

urlpatterns = router.urls
