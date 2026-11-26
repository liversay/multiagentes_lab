El código y los tests proporcionados cumplen con los requisitos especificados. Aquí hay una breve evaluación:

1. **Requisito: Agregar prioridad alta, media o baja; por defecto media. Rechazar otra prioridad con ValueError.**:
   - La función `_validar_prioridad` asegura que la prioridad sea válida antes de agregar una tarea. Si la prioridad no es uno de los permitidos, se genera un `ValueError`.

2. **Requisito: Crear filtrar_por_prioridad(tareas, prioridad). Conservar agregar(tareas, titulo) y pendientes(tareas)**:
   - La función `filtrar_por_prioridad` filtra las tareas por prioridad y las devuelve como una lista. Las funciones `agregar` y `pendientes` permanecen sin cambios.

3. **Requisito: Agregar pruebas válidas, inválidas y de regresión**:
   - Los tests cubren varios aspectos, incluyendo:
     - Pruebas para el método `agregar` con diferentes prioridades y títulos.
     - Pruebas para la validación de prioridades inválidas.
     - Pruebas para el método `filtrar_por_prioridad` con prioridades válidas y inválidas.
     - Pruebas de regresión para asegurar que el comportamiento de las funciones no cambia.

4. **Requisito: No afirmes que todo pasa si no hay evidencia**:
   - Los tests se basan en verificaciones explícitas y se han utilizado excepciones para verificar errores.

El código y los tests están bien estructurados y funcionan correctamente según los requisitos propuestos.