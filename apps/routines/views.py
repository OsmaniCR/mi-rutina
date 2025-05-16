from rest_framework import viewsets, permissions, status
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from .models import Routine, RoutineDetail, Exercise
from .serializers import (
    RoutineSerializer,
    RoutineDetailSerializer,
    ExerciseSerializer,
    ExerciseListSerializer,
    RoutineCreateSerializer,
)


class RoutineViewSet(viewsets.ModelViewSet):
    queryset = Routine.objects.all()
    serializer_class = RoutineSerializer
    permission_classes = [DjangoModelPermissions]
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    search_fields = ["name", "description"]
    ordering_fields = ["created_at", "updated_at"]
    filterset_fields = ["dow"]


class RoutineDetailViewSet(viewsets.ModelViewSet):
    queryset = RoutineDetail.objects.all()
    serializer_class = RoutineDetailSerializer
    permission_classes = [DjangoModelPermissions]
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    search_fields = ["routine__name", "exercise__name"]
    ordering_fields = ["created_at", "updated_at"]
    filterset_fields = ["routine__dow"]


class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    permission_classes = [DjangoModelPermissions]
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    search_fields = ["name", "description"]
    ordering_fields = ["created_at", "updated_at"]
    filterset_fields = []


class UserRoutineViewSet(viewsets.ModelViewSet):
    serializer_class = RoutineCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        print(self.request.user)
        return Routine.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True, methods=["get"])
    def exercises(self, request, pk=None):
        routine = self.get_object()
        exercises = RoutineDetail.objects.filter(routine=routine)
        serializer = RoutineDetailSerializer(exercises, many=True)
        return Response(serializer.data)


class ExerciseListViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseListSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [SearchFilter]
    search_fields = ["name", "description"]
