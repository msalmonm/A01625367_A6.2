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