import unittest
from tareas import agregar, pendientes

class TestTareas(unittest.TestCase):
    def test_agregar(self):
        tareas = []
        self.assertEqual(agregar(tareas, "Leer")["id"], 1)
    def test_titulo_vacio(self):
        with self.assertRaises(ValueError):
            agregar([], "   ")

if __name__ == "__main__":
    unittest.main()
