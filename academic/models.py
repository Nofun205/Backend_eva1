from django.db import models

class Teacher(models.Model):
    """Modelo que representa a un Docente en el sistema"""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Course(models.Model):
    """Modelo que representa una Asignatura, vinculada a un Docente (1:N)"""
    name = models.CharField(max_length=200)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='courses')

    def __str__(self):
        return self.name

class Student(models.Model):
    """Modelo que representa a un Estudiante en el sistema"""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class StudentCourse(models.Model):
    """Modelo de tabla intermedia para la relación N:M entre Estudiantes y Cursos (Inscripciones)"""
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='enrollments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments')

    class Meta:
        # Asegura que un estudiante no se inscriba dos veces en el mismo curso
        unique_together = ('student', 'course')

    def __str__(self):
        return f"{self.student} en {self.course}"
