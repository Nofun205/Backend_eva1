# Uso de Inteligencia Artificial

A continuación se detallan los prompts exactos utilizados en una herramienta de IA (Gemini) para generar los entregables solicitados.

## 1. Diseño de Plantillas y Maquetación en HTML/Bootstrap

**Prompt utilizado:**
```text
Actúa como un desarrollador web experto. Necesito que diseñes una plantilla base en HTML utilizando Bootstrap 5 (vía CDN). La plantilla debe tener:
- Una barra de navegación superior (navbar) de color oscuro con enlaces a "Cursos" y "Estudiantes".
- Un contenedor principal para el contenido.
- El diseño debe ser limpio y responsivo.

Luego, genérame una vista "index.html" que extienda de esta plantilla base y muestre un mensaje de bienvenida usando la clase 'jumbotron' o similar en Bootstrap 5.

Finalmente, genérame una vista "courses.html" y otra "students.html" que extiendan de la base. Ambas deben contener una tabla estilizada con Bootstrap (table-striped, table-hover, cabecera oscura). En la de cursos las columnas serán ID, Nombre del Curso y Profesor Asignado. En la de estudiantes serán ID, Nombre y Apellido.
```

**Respuesta generada por la IA:**
La IA generó la estructura HTML base que fue posteriormente adaptada e integrada con el sistema de templates de Django (agregando los tags `{% extends %}` y `{% block %}`). El código generado se encuentra en los archivos `base.html`, `index.html`, `courses.html` y `students.html`.

## 2. Generación de Estructura de Datos Simulada en JSON

**Prompt utilizado:**
```text
Actúa como un generador de datos de prueba. Necesito un archivo JSON ('mock_data.json') que contenga datos ficticios para un sistema de gestión académica. Los datos deben seguir la estructura requerida por Django "fixtures" para ser cargados en la base de datos (con los campos "model", "pk", y "fields").

Genera los datos para los siguientes modelos de la aplicación "academic":
1. "academic.teacher" (campos: first_name, last_name). Genera 2 profesores.
2. "academic.course" (campos: name, teacher - que es el ID del profesor). Genera 3 cursos asignados a los profesores anteriores.
3. "academic.student" (campos: first_name, last_name). Genera 4 estudiantes.
4. "academic.studentcourse" (campos: student, course). Asigna a cada estudiante a 1 o 2 cursos.

Asegúrate de que las IDs coincidan correctamente. El formato de salida debe ser un arreglo de objetos JSON puro.
```

**Respuesta generada por la IA:**
La IA generó el archivo `mock_data.json` que contiene un arreglo válido con los datos listos para ser importados mediante `loaddata` en Django. (El archivo JSON resultante se adjunta en la entrega y fue utilizado para poblar la base de datos).

## 3. Mejora Visual y Estilos Cálidos en el Frontend

**Prompt utilizado:**
```text
Actúa como diseñador UI/UX. Mejora las plantillas HTML que hicimos añadiendo un diseño mucho más "cálido", elegante y moderno. Utiliza colores naranjas, amarillos y fondos suaves (fdebd0, d35400, f39c12). Usa estilos CSS "card-custom" para redondear las tablas y mejorar la experiencia de usuario.
```

**Respuesta generada por la IA:**
La IA reescribió las clases CSS y la estructura HTML en `base.html` y las tablas, aplicando paletas cálidas y botones estilizados que actualmente se visualizan en el proyecto.

## 4. Implementación de CRUD Completo con Fetch (SPA)

**Prompt utilizado:**
```text
Actúa como desarrollador Frontend con JavaScript. Modifica las vistas HTML (students.html, courses.html y la nueva enrollments.html) para que sean aplicaciones SPA (Single Page Application). 
Agrega botones de Editar y Eliminar en cada fila de las tablas. Utiliza la API Fetch() nativa de JS para enviar peticiones POST, PUT y DELETE hacia mis endpoints de Django REST Framework, recargando los datos dinámicamente sin refrescar la página.
```

**Respuesta generada por la IA:**
La IA generó todo el bloque `<script>` de lógica asíncrona, capturando eventos de los formularios, haciendo el mapeo de IDs y llamando a los endpoints correspondientes de la API para mantener el sistema completamente funcional en tiempo real.
