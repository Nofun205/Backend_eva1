from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Inicializamos el enrutador de DRF para crear automáticamente las URLs de la API
router = DefaultRouter()
# Registramos cada ViewSet con su ruta correspondiente
router.register(r'teachers', views.TeacherViewSet)
router.register(r'courses', views.CourseViewSet)
router.register(r'students', views.StudentViewSet)
router.register(r'enrollments', views.StudentCourseViewSet)

urlpatterns = [
    # Rutas para la API DRF (Retornan JSON)
    path('api/', include(router.urls)),
    
    # Rutas para la Interfaz Web (Retornan HTML - "Enmascaramiento")
    # Estas vistas consumen visualmente la API mediante JS (Fetch)
    path('', views.index_view, name='index'),
    path('courses/', views.courses_view, name='courses'),
    path('students/', views.students_view, name='students'),
]
