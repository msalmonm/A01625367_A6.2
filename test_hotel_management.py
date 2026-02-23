import unittest
import os
from hotel_management import Hotel, Customer, Reservation, FileManager

class TestHotelSystem(unittest.TestCase):
    """Suite de pruebas para el Sistema de Reservaciones."""

    def setUp(self):
        """Configuración inicial: Limpiar archivos antes de cada prueba."""
        self.files = ["hotels.json", "customers.json", "reservations.json"]
        for f in self.files:
            if os.path.exists(f):
                os.remove(f)

    def test_load_non_existent_file(self):
        """Caso Positivo: Cargar archivo que no existe."""
        data = FileManager.load_data("non_existent.json")
        self.assertEqual(data, [])

    def test_corrupted_json_negative(self):
        """Caso Negativo: Manejo de archivos JSON corruptos."""
        with open("hotels.json", "w", encoding='utf-8') as f:
            f.write("{ 'invalid': json ...")
        data = FileManager.load_data("hotels.json")
        self.assertEqual(data, [])

    def test_create_and_display_hotel(self):
        """Caso Positivo: Crear hotel (incluyendo rooms)."""
        Hotel.create_hotel(101, "Hotel Sol", "Cancun", 50)
        hotels = FileManager.load_data("hotels.json")
        self.assertEqual(len(hotels), 1)
        self.assertEqual(hotels[0]['rooms'], 50)

    def test_delete_non_existent_hotel_negative(self):
        """Caso Negativo: Borrar hotel inexistente."""
        Hotel.create_hotel(1, "Existente", "CDMX", 10)
        Hotel.delete_hotel(999)
        hotels = FileManager.load_data("hotels.json")
        self.assertEqual(len(hotels), 1)

    def test_modify_customer_info(self):
        """Caso Positivo: Modificar cliente."""
        Customer.create_customer(1, "Juan", "juan@test.com")
        Customer.modify_customer(1, name="Juan Perez")
        customers = FileManager.load_data("customers.json")
        self.assertEqual(customers[0]['name'], "Juan Perez")

    def test_modify_non_existent_customer_negative(self):
        """Caso Negativo: Modificar cliente inexistente."""
        Customer.modify_customer(888, name="Error")
        customers = FileManager.load_data("customers.json")
        self.assertEqual(len(customers), 0)

    def test_create_reservation_success(self):
        """Caso Positivo: Crear reservación."""
        Hotel.create_hotel(1, "H1", "Loc", 20)
        Customer.create_customer(1, "C1", "E1")
        Reservation.create_reservation(500, 1, 1)
        res = FileManager.load_data("reservations.json")
        self.assertEqual(len(res), 1)

    def test_res_invalid_customer_negative(self):
        """Caso Negativo: Reservar con ID de cliente inválido."""
        Hotel.create_hotel(1, "H1", "Loc", 20)
        Reservation.create_reservation(501, 999, 1)
        res = FileManager.load_data("reservations.json")
        self.assertEqual(len(res), 1)

    def test_cancel_non_existent_reservation_negative(self):
        """Caso Negativo: Cancelar reservación inexistente."""
        Reservation.cancel_reservation(777)
        res = FileManager.load_data("reservations.json")
        self.assertEqual(len(res), 0)

    def test_delete_customer_logic(self):
        """Caso Positivo: Borrar cliente."""
        Customer.create_customer(2, "Ana", "ana@test.com")
        Customer.delete_customer(2)
        customers = FileManager.load_data("customers.json")
        self.assertEqual(len(customers), 0)

    def tearDown(self):
        """Limpiar archivos después de las pruebas."""
        for f in self.files:
            if os.path.exists(f):
                os.remove(f)

if __name__ == "__main__":
    unittest.main()