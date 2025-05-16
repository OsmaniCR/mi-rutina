from django.db import models
from django.contrib.auth.models import User


class Routine(models.Model):

    DAYS_OF_WEEK = [
        ("MONDAY", "Lunes"),
        ("TUESDAY", "Martes"),
        ("WEDNESDAY", "Miércoles"),
        ("THURSDAY", "Jueves"),
        ("FRIDAY", "Viernes"),
        ("SATURDAY", "Sábado"),
        ("SUNDAY", "Domingo"),
    ]

    name = models.CharField(max_length=255, verbose_name="Nombre")
    description = models.TextField(verbose_name="Descripción")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dow = models.CharField(
        max_length=255,
        choices=DAYS_OF_WEEK,
        verbose_name="Día de la semana",
    )
    start_time = models.TimeField(verbose_name="Hora de inicio")
    end_time = models.TimeField(verbose_name="Hora de fin")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - ({self.id})"


class Exercise(models.Model):
    # TODO: Aquí se pudierar agrupar por grupos musculares, etc
    name = models.CharField(max_length=255, verbose_name="Nombre")
    description = models.TextField(verbose_name="Descripción")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - ({self.id})"


class RoutineDetail(models.Model):
    """
    This model is used to store the details of a routine.
    """

    routine = models.ForeignKey(
        Routine, on_delete=models.CASCADE, verbose_name="Rutina"
    )
    exercise = models.ForeignKey(
        Exercise, on_delete=models.CASCADE, verbose_name="Ejercicio"
    )
    sets = models.IntegerField(verbose_name="Series")
    reps = models.IntegerField(verbose_name="Repeticiones")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.routine.name} - {self.exercise.name}"
