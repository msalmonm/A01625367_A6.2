import unittest
from hotel_management import Hotel, FileManager

class TestHotel(unittest.TestCase):
    """Pruebas para la clase Hotel."""
    def test_create_hotel(self):
        """Prueba creación exitosa."""
        Hotel.create_hotel(1, "Test Hotel", "Cancun")
        data = FileManager.load_data("hotels.json")
        self.assertTrue(any(h['id'] == 1 for h in data))