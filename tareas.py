def agregar(tareas, titulo):
    titulo = titulo.strip()
    if not titulo:
        raise ValueError("Título obligatorio")
    tarea = {"id": len(tareas) + 1, "titulo": titulo}
    tareas.append(tarea)
    return tarea

def pendientes(tareas):
    return list(tareas)
