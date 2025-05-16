from rest_framework import serializers
from .models import Routine, RoutineDetail, Exercise


class RoutineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Routine
        fields = "__all__"


class RoutineDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoutineDetail
        fields = "__all__"


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = "__all__"


class ExerciseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ["id", "name", "description"]


class RoutineDetailCreateSerializer(serializers.ModelSerializer):
    exercise_id = serializers.IntegerField(write_only=True)
    exercise_name = serializers.CharField(source="exercise.name", read_only=True)

    class Meta:
        model = RoutineDetail
        fields = ["id", "exercise_id", "exercise_name", "sets", "reps"]
        read_only_fields = ["id", "exercise_name"]

    def validate(self, data):
        if data["sets"] <= 0:
            raise serializers.ValidationError("El número de series debe ser mayor a 0")
        if data["reps"] <= 0:
            raise serializers.ValidationError(
                "El número de repeticiones debe ser mayor a 0"
            )
        return data


class RoutineCreateSerializer(serializers.ModelSerializer):
    exercises = RoutineDetailCreateSerializer(many=True, required=False)
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Routine
        fields = [
            "id",
            "name",
            "description",
            "user",
            "dow",
            "start_time",
            "end_time",
            "exercises",
        ]
        read_only_fields = ["id", "user"]

    def validate(self, data):
        if data["start_time"] >= data["end_time"]:
            raise serializers.ValidationError(
                "La hora de inicio debe ser anterior a la hora de fin"
            )
        return data

    def create(self, validated_data):
        exercises_data = validated_data.pop("exercises", [])
        routine = Routine.objects.create(**validated_data)

        for exercise_data in exercises_data:
            exercise_id = exercise_data.pop("exercise_id")
            exercise = Exercise.objects.get(id=exercise_id)
            RoutineDetail.objects.create(
                routine=routine, exercise=exercise, **exercise_data
            )

        return routine
