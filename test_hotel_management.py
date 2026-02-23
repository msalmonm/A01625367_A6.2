import unittest
from hotel_management import Hotel, FileManager

class TestHotel(unittest.TestCase):
    """Pruebas para la clase Hotel."""
    def test_create_hotel(self):
        """Prueba creación exitosa."""
        Hotel.create_hotel(1, "Test Hotel", "Cancun")
        data = FileManager.load_data("hotels.json")
        self.assertTrue(any(h['id'] == 1 for h in data))
        
def test_invalid_file_handling(self):
        """Caso negativo: Archivo con JSON corrupto (Req 5)."""
        with open("hotels.json", "w") as f:
            f.write("---") # JSON inválido
        data = FileManager.load_data("hotels.json")
        self.assertEqual(data, []) # El programa debe continuar