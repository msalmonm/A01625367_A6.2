"""
Módulo de Gestión de Hoteles, Clientes y Reservaciones.
Cumple con los estándares PEP8, Pylint y Flake8.
"""
import json
import os


class FileManager:
    """Clase auxiliar para manejar operaciones de archivos JSON."""

    @staticmethod
    def load_data(filename):
        """Carga datos desde un archivo JSON. Maneja errores de datos (Req 5)."""
        if not os.path.exists(filename):
            return []
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                return json.load(file)
        except (json.JSONDecodeError, IOError):
            print(f"Error: Datos inválidos en {filename}. Iniciando vacío.")
            return []

    @staticmethod
    def save_data(filename, data):
        """Guarda datos en un archivo JSON."""
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=4)
        except IOError as error:
            print(f"Error al guardar en {filename}: {error}")


class Hotel:
    """Clase que representa un Hotel."""
    FILENAME = "hotels.json"

    def __init__(self, hotel_id, name, location, rooms):
        self.hotel_id = hotel_id
        self.name = name
        self.location = location
        self.rooms = rooms

    @classmethod
    def create_hotel(cls, hotel_id, name, location, rooms):
        """Crea y persiste un nuevo hotel."""
        hotels = FileManager.load_data(cls.FILENAME)
        hotels.append({
            "id": hotel_id, "name": name,
            "location": location, "rooms": rooms
        })
        FileManager.save_data(cls.FILENAME, hotels)

    @classmethod
    def delete_hotel(cls, hotel_id):
        """Elimina un hotel por ID."""
        hotels = FileManager.load_data(cls.FILENAME)
        hotels = [h for h in hotels if h['id'] != hotel_id]
        FileManager.save_data(cls.FILENAME, hotels)

    @classmethod
    def display_hotel_info(cls, hotel_id):
        """Muestra la información de un hotel específico."""
        hotels = FileManager.load_data(cls.FILENAME)
        hotel = next((h for h in hotels if h['id'] == hotel_id), None)
        if hotel:
            print(f"Hotel: {hotel['name']}, Ubicación: {hotel['location']}")
        return hotel

    @classmethod
    def modify_hotel_info(cls, hotel_id, **kwargs):
        """Modifica los atributos de un hotel."""
        hotels = FileManager.load_data(cls.FILENAME)
        for hotel in hotels:
            if hotel['id'] == hotel_id:
                hotel.update(kwargs)
        FileManager.save_data(cls.FILENAME, hotels)


class Customer:
    """Clase que representa un Cliente."""
    FILENAME = "customers.json"

    @classmethod
    def create_customer(cls, customer_id, name, email):
        """Registra un nuevo cliente."""
        customers = FileManager.load_data(cls.FILENAME)
        customers.append({"id": customer_id, "name": name, "email": email})
        FileManager.save_data(cls.FILENAME, customers)

    @classmethod
    def delete_customer(cls, customer_id):
        """Elimina un cliente por ID."""
        customers = FileManager.load_data(cls.FILENAME)
        customers = [c for c in customers if c['id'] != customer_id]
        FileManager.save_data(cls.FILENAME, customers)

    @classmethod
    def modify_customer(cls, customer_id, **kwargs):
        """Modifica la información de un cliente."""
        customers = FileManager.load_data(cls.FILENAME)
        for cust in customers:
            if cust['id'] == customer_id:
                cust.update(kwargs)
        FileManager.save_data(cls.FILENAME, customers)

    @classmethod
    def display_customer_info(cls, customer_id):
        """Muestra los detalles de un cliente."""
        customers = FileManager.load_data(cls.FILENAME)
        customer = next((c for c in customers if c['id'] == customer_id), None)
        if customer:
            print(f"Cliente: {customer['name']}, Email: {customer['email']}")
        return customer


class Reservation:
    """Clase que representa una Reservación."""
    FILENAME = "reservations.json"

    @classmethod
    def create_reservation(cls, reservation_id, customer_id, hotel_id):
        """Crea una reservación vinculando cliente y hotel."""
        reservations = FileManager.load_data(cls.FILENAME)
        reservations.append({
            "res_id": reservation_id,
            "customer_id": customer_id,
            "hotel_id": hotel_id
        })
        FileManager.save_data(cls.FILENAME, reservations)

    @classmethod
    def cancel_reservation(cls, reservation_id):
        """Cancela (elimina) una reservación."""
        reservations = FileManager.load_data(cls.FILENAME)
        reservations = [r for r in reservations if r['res_id'] != reservation_id]
        FileManager.save_data(cls.FILENAME, reservations)