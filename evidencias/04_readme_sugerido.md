# README

## Contenido

- **Funciones**
  - `agregar(tareas, titulo, prioridad="media")`
  - `pendientes(tareas)`
  - `filtrar_por_prioridad(tareas, prioridad)`

- **Prioridades Permitidas**
  - Alta
  - Media
  - Baja

- **Valor por defecto**
  - Prioridad: "media"

- **Rechazo de valores inválidos**
  - Si la prioridad proporcionada no es "alta", "media" o "baja", se lanzará una excepción `ValueError` con el mensaje "Prioridad no válida".

- **Pasos**
  1. **Agregar tarea**
     - Limpia el título y verifica que no esté vacío.
     - Crea un diccionario con el identificador único y la prioridad por defecto.
     - Agrega la tarea a la lista de tareas.
     - Devuelve la tarea recién agregada.

  2. **Tareas pendientes**
     - Devuelve una copia de la lista de tareas.

  3. **Filtrar por prioridad**
     - Crea un nuevo listado de tareas que coinciden con la prioridad proporcionada.
     - Devuelve el listado filtrado.

- **Criterios de aceptación y pruebas**
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

## Instalación y Uso

No es necesario instalar ningún paquete adicional. El código está comprensible y puede ser utilizado directamente en un entorno de desarrollo.

## Ejemplos de Uso

### Agregar Tarea
```python
tareas = []
agregar(tareas, "Comprar leche", "alta")
agregar(tareas, "Lavar la ropa", "media")
```

### Pendientes
```python
pendientes_tareas = pendientes(tareas)
print(pendientes_tareas)
```

### Filtrar por Prioridad
```python
tareas_altas = filtrar_por_prioridad(tareas, "alta")
print(tareas_altas)
```

## Revisión y Pruebas

Para garantizar la calidad del código, se sugiere ejecutar las pruebas proporcionadas en el `PLAN` para verificar que la implementación cumple con los criterios de aceptación.

## Dependencias

No se requiere ninguna dependencia adicional para ejecutar este código.