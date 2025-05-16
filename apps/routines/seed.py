from django.contrib.auth.models import User
from django.utils import timezone
from faker import Faker
import random
from datetime import time

from .models import Routine, Exercise, RoutineDetail

fake = Faker("es_ES")


def create_users(num_users=5):
    """Crear usuarios de prueba"""
    users = []
    for _ in range(num_users):
        user = User.objects.create_user(
            username=fake.user_name(),
            email=fake.email(),
            password="password123",
            first_name=fake.first_name(),
            last_name=fake.last_name(),
        )
        users.append(user)
    return users


def create_exercises(num_exercises=20):
    """Crear ejercicios de prueba"""
    exercises = []
    exercise_names = [
        "Sentadillas",
        "Flexiones",
        "Plancha",
        "Burpees",
        "Zancadas",
        "Dominadas",
        "Press de banca",
        "Peso muerto",
        "Remo",
        "Abdominales",
        "Extensiones de tríceps",
        "Curl de bíceps",
        "Elevaciones laterales",
        "Extensiones de pierna",
        "Curl de pierna",
        "Press militar",
        "Pull-ups",
        "Push-ups",
        "Mountain climbers",
        "Jumping jacks",
    ]

    for name in exercise_names:
        exercise = Exercise.objects.create(
            name=name, description=fake.text(max_nb_chars=200)
        )
        exercises.append(exercise)
    return exercises


def create_routines(users, exercises, num_routines_per_user=3):
    """Crear rutinas de prueba"""
    routines = []
    days_of_week = [day[0] for day in Routine.DAYS_OF_WEEK]

    for user in users:
        for _ in range(num_routines_per_user):
            start_hour = random.randint(6, 20)
            start_minute = random.choice([0, 15, 30, 45])
            end_hour = start_hour + random.randint(1, 2)
            end_minute = random.choice([0, 15, 30, 45])

            routine = Routine.objects.create(
                name=fake.catch_phrase(),
                description=fake.text(max_nb_chars=200),
                user=user,
                dow=random.choice(days_of_week),
                start_time=time(start_hour, start_minute),
                end_time=time(end_hour, end_minute),
            )
            routines.append(routine)
    return routines


def create_routine_details(routines, exercises):
    """Crear detalles de rutinas de prueba"""
    for routine in routines:
        # Agregar entre 3 y 6 ejercicios por rutina
        num_exercises = random.randint(3, 6)
        selected_exercises = random.sample(exercises, num_exercises)

        for exercise in selected_exercises:
            RoutineDetail.objects.create(
                routine=routine,
                exercise=exercise,
                sets=random.randint(3, 5),
                reps=random.randint(8, 15),
            )


def seed_database():
    """Función principal para poblar la base de datos"""
    print("Creando usuarios...")
    users = create_users()

    print("Creando ejercicios...")
    exercises = create_exercises()

    print("Creando rutinas...")
    routines = create_routines(users, exercises)

    print("Creando detalles de rutinas...")
    create_routine_details(routines, exercises)

    print("¡Base de datos poblada exitosamente!")


if __name__ == "__main__":
    seed_database()
