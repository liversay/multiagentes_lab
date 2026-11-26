import unittest
from tareas import agregar, pendientes, filtrar_por_prioridad

class TestTareas(unittest.TestCase):
    def test_agregar(self):
        tareas = []
        self.assertEqual(agregar(tareas, "Leer")["id"], 1)
    def test_titulo_vacio(self):
        with self.assertRaises(ValueError):
            agregar([], "   ")
    def test_prioridad_por_defecto(self):
        self.assertEqual(agregar([], "Leer")["prioridad"], "media")
    def test_prioridades_validas(self):
        for prioridad in ("alta", "media", "baja"):
            with self.subTest(prioridad=prioridad):
                tarea = agregar([], "Leer", prioridad)
                self.assertEqual(tarea["prioridad"], prioridad)
    def test_prioridad_invalida(self):
        tareas = []
        with self.assertRaises(ValueError):
            agregar(tareas, "Leer", "urgente")
        self.assertEqual(tareas, [])
    def test_filtrar_por_prioridad(self):
        tareas = []
        agregar(tareas, "Leer", "alta")
        agregar(tareas, "Correr")
        agregar(tareas, "Dormir", "baja")
        filtradas = filtrar_por_prioridad(tareas, "alta")
        self.assertEqual([t["titulo"] for t in filtradas], ["Leer"])
    def test_filtrar_prioridad_invalida(self):
        with self.assertRaises(ValueError):
            filtrar_por_prioridad([], "urgente")
    def test_pendientes_regresion(self):
        tareas = []
        agregar(tareas, "  Leer  ")
        copia = pendientes(tareas)
        self.assertEqual(copia, tareas)
        self.assertIsNot(copia, tareas)
        self.assertEqual(copia[0]["titulo"], "Leer")

if __name__ == "__main__":
    unittest.main()
