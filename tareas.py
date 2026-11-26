PRIORIDADES = ("alta", "media", "baja")

def _validar_prioridad(prioridad):
    if prioridad not in PRIORIDADES:
        raise ValueError("Prioridad no válida: use alta, media o baja")

def agregar(tareas, titulo, prioridad="media"):
    titulo = titulo.strip()
    if not titulo:
        raise ValueError("Título obligatorio")
    _validar_prioridad(prioridad)
    tarea = {"id": len(tareas) + 1, "titulo": titulo, "prioridad": prioridad}
    tareas.append(tarea)
    return tarea

def pendientes(tareas):
    return list(tareas)

def filtrar_por_prioridad(tareas, prioridad):
    _validar_prioridad(prioridad)
    return [t for t in tareas if t["prioridad"] == prioridad]
