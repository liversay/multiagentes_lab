A continuación, proporciono el código actualizado con las nuevas características, incluyendo la función `filtrar_por_prioridad` y las pruebas correspondientes.

```python
def agregar(tareas, titulo):
    titulo = titulo.strip()
    if not titulo:
        raise ValueError("Título obligatorio")
    tarea = {"id": len(tareas) + 1, "titulo": titulo, "prioridad": "media"}
    tareas.append(tarea)
    return tarea

def pendientes(tareas):
    return list(tareas)

def filtrar_por_prioridad(tareas, prioridad):
    valid_priorities = ["alta", "media", "baja"]
    if prioridad not in valid_priorities:
        raise ValueError("Prioridad no válida")
    filtered_tasks = [task for task in tareas if task["prioridad"] == prioridad]
    return filtered_tasks

# Pruebas

# Pruebas válidas
def test_agregar_tarea():
    tareas = []
    tarea = agregar(tareas, "Comprar leche")
    assert tarea == {"id": 1, "titulo": "Comprar leche", "prioridad": "media"}
    assert tareas == [{"id": 1, "titulo": "Comprar leche", "prioridad": "media"}]

def test_pendientes():
    tareas = [{"id": 1, "titulo": "Comprar leche", "prioridad": "media"}]
    pendientes_tareas = pendientes(tareas)
    assert pendientes_tareas == [{"id": 1, "titulo": "Comprar leche", "prioridad": "media"}]

def test_filtrar_por_prioridad():
    tareas = [
        {"id": 1, "titulo": "Comprar leche", "prioridad": "media"},
        {"id": 2, "titulo": "Estudiar", "prioridad": "alta"},
        {"id": 3, "titulo": "Hacer ejercicio", "prioridad": "baja"}
    ]
    media_tareas = filtrar_por_prioridad(tareas, "media")
    assert media_tareas == [{"id": 1, "titulo": "Comprar leche", "prioridad": "media"}]

    alta_tareas = filtrar_por_prioridad(tareas, "alta")
    assert alta_tareas == [{"id": 2, "titulo": "Estudiar", "prioridad": "alta"}]

    baja_tareas = filtrar_por_prioridad(tareas, "baja")
    assert baja_tareas == [{"id": 3, "titulo": "Hacer ejercicio", "prioridad": "baja"}]

# Pruebas inválidas
def test_agregar_tarea_vacio_titulo():
    tareas = []
    try:
        agregar(tareas, "")
    except ValueError as e:
        assert str(e) == "Título obligatorio"
    else:
        assert False, "Debería lanzar una excepción"

def test_filtrar_por_prioridad_invalida():
    tareas = []
    try:
        filtrar_por_prioridad(tareas, "invalida")
    except ValueError as e:
        assert str(e) == "Prioridad no válida"
    else:
        assert False, "Debería lanzar una excepción"

# Pruebas de regresión
def test_agregar_y_filtrar():
    tareas = []
    agregar(tareas, "Ir a la tienda")
    pendientes_tareas = pendientes(tareas)
    assert pendientes_tareas == [{"id": 1, "titulo": "Ir a la tienda", "prioridad": "media"}]

    media_tareas = filtrar_por_prioridad(tareas, "media")
    assert media_tareas == [{"id": 1, "titulo": "Ir a la tienda", "prioridad": "media"}]

    tarea_original = pendientes_tareas[0]
    media_tarea_filtrada = media_tareas[0]
    assert tarea_original == media_tarea_filtrada
```

Este código incluye las nuevas funciones y pruebas especificadas, garantizando que la prioridad de las tareas sea validada y que se puedan filtrar por esta prioridad de manera adecuada.