import json
import os

class FileManager:
    """Manejo de persistencia de datos en archivos JSON."""
    @staticmethod
    def load_data(filename):
        """Carga datos y maneja archivos corruptos o inexistentes."""
        if not os.path.exists(filename):
            return []
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                return json.load(file)
        except (json.JSONDecodeError, IOError):
            print(f"Error: Datos inválidos en {filename}.")
            return []

    @staticmethod
    def save_data(filename, data):
        """Guarda datos en formato JSON."""
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)

class Hotel:
    """Clase para gestionar hoteles."""
    FILENAME = "hotels.json"

    def __init__(self, hotel_id, name, location):
        self.hotel_id = hotel_id
        self.name = name
        self.location = location

    @classmethod
    def create_hotel(cls, h_id, name, loc):
        """Crea y guarda un hotel."""
        hotels = FileManager.load_data(cls.FILENAME)
        hotels.append({"id": h_id, "name": name, "location": loc})
        FileManager.save_data(cls.FILENAME, hotels)

class Customer:
    """Clase para gestionar clientes."""
    FILENAME = "customers.json"

    @classmethod
    def create_customer(cls, c_id, name, email):
        """Registra un nuevo cliente."""
        customers = FileManager.load_data(cls.FILENAME)
        customers.append({"id": c_id, "name": name, "email": email})
        FileManager.save_data(cls.FILENAME, customers)