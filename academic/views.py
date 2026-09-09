from django.shortcuts import render
from rest_framework import viewsets
from .models import Teacher, Course, Student, StudentCourse
from .serializers import TeacherSerializer, CourseSerializer, StudentSerializer, StudentCourseSerializer

# ==========================================
# VISTAS DE RENDERIZADO HTML (Enmascaramiento)
# ==========================================
# Estas vistas simplemente retornan las plantillas HTML
# El consumo real de datos se hace vía Fetch API en el navegador

def index_view(request):
    """Renderiza la página de inicio (soluciona el error 404 en la ruta /)"""
    return render(request, 'academic/index.html')

def courses_view(request):
    """Renderiza la tabla de cursos (los datos se llenan vía JS asíncrono)"""
    return render(request, 'academic/courses.html')

def students_view(request):
    """Renderiza la tabla de estudiantes (los datos se llenan vía JS asíncrono)"""
    return render(request, 'academic/students.html')

def enrollments_view(request):
    """Renderiza la tabla de inscripciones (relación Estudiante-Curso)"""
    return render(request, 'academic/enrollments.html')

# ==========================================
# ENDPOINTS DE API (Django REST Framework)
# ==========================================
# Estos ViewSets manejan automáticamente el CRUD y exponen JSON

class TeacherViewSet(viewsets.ModelViewSet):
    """Endpoint para operaciones CRUD del modelo Teacher"""
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class CourseViewSet(viewsets.ModelViewSet):
    """Endpoint para operaciones CRUD del modelo Course"""
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class StudentViewSet(viewsets.ModelViewSet):
    """Endpoint para operaciones CRUD del modelo Student"""
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentCourseViewSet(viewsets.ModelViewSet):
    """Endpoint para operaciones CRUD de las inscripciones (StudentCourse)"""
    queryset = StudentCourse.objects.all()
    serializer_class = StudentCourseSerializer
