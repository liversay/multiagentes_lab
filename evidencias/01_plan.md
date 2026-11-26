**1) Contrato de API:**

| Nombre de la función | Parámetros | Descripción |
|-----------------------|------------|-------------|
| agregar(tareas, titulo) | tareas (list), titulo (str) | Añade una tarea a la lista de tareas con un identificador único y una prioridad por defecto de "media". |
| pendientes(tareas) | tareas (list) | Devuelve una lista de tareas pendientes. |
| filtrar_por_prioridad(tareas, prioridad) | tareas (list), prioridad (str) | Devuelve una lista de tareas filtradas por una prioridad específica. |

**2) Prioridades permitidas:**

- Alta
- Media
- Baja

**3) Valor por defecto:**

- Prioridad: "media"

**4) Rechazo de valores inválidos:**

- Si la prioridad proporcionada no es "alta", "media" o "baja", se lanzará una excepción `ValueError` con el mensaje "Prioridad no válida".

**5) Pasos:**

1. **Agregar tarea:**
   - Limpia el título y verifica que no esté vacío.
   - Crea un diccionario con el identificador único y la prioridad por defecto.
   - Agrega la tarea a la lista de tareas.
   - Devuelve la tarea recién agregada.

2. **Tareas pendientes:**
   - Devuelve una copia de la lista de tareas.

3. **Filtrar por prioridad:**
   - Crea un nuevo listado de tareas que coinciden con la prioridad proporcionada.
   - Devuelve el listado filtrado.

**6) Criterios de aceptación y pruebas:**

- Pruebas válidas:
  - Agregar una tarea con una prioridad válida.
  - Filtrar por prioridad válida.
  - Pendientes devuelve todas las tareas pendientes.

- Pruebas inválidas:
  - Intentar filtrar por una prioridad inválida.
  - Intentar agregar una tarea con un título vacío.

- Pruebas de regresión:
  - Agregar una tarea, filtrar por prioridad y verificar que la tarea pendiente no se pierde.
  - Filtrar por una prioridad y verificar que la tarea con esa prioridad se muestra correctamente.