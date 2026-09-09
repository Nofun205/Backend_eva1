from rest_framework import serializers
from .models import Teacher, Course, Student, StudentCourse

class TeacherSerializer(serializers.ModelSerializer):
    """Serializador para convertir el modelo Teacher a JSON y viceversa"""
    class Meta:
        model = Teacher
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    """Serializador para el modelo Course. 
    Muestra los detalles del profesor al leer (read_only), 
    pero permite enviar un teacher_id para escribir."""
    teacher = TeacherSerializer(read_only=True)
    teacher_id = serializers.PrimaryKeyRelatedField(
        queryset=Teacher.objects.all(), source='teacher', write_only=True
    )

    class Meta:
        model = Course
        fields = ['id', 'name', 'teacher', 'teacher_id']

class StudentSerializer(serializers.ModelSerializer):
    """Serializador para convertir el modelo Student a JSON y viceversa"""
    class Meta:
        model = Student
        fields = '__all__'

class StudentCourseSerializer(serializers.ModelSerializer):
    """Serializador para las inscripciones. 
    Al leer, trae la información completa del estudiante y el curso."""
    student = StudentSerializer(read_only=True)
    course = CourseSerializer(read_only=True)
    
    student_id = serializers.PrimaryKeyRelatedField(
        queryset=Student.objects.all(), source='student', write_only=True
    )
    course_id = serializers.PrimaryKeyRelatedField(
        queryset=Course.objects.all(), source='course', write_only=True
    )

    class Meta:
        model = StudentCourse
        fields = ['id', 'student', 'course', 'student_id', 'course_id']
