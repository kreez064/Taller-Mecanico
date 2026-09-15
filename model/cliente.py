from model.persona import Persona # Importa la clase Persona desde el modulo model.persona


class Cliente: # Define la clase Cliente para representar a un cliente del taller
    def __init__(self, persona: Persona): # Constructor que recibe un objeto Persona asociado al cliente
        self.__persona = persona # Asigna el objeto Persona a un atributo privado

    def tiene_deuda(self) -> bool: # Metodo para verificar si el cliente tiene deuda pendiente
        return False # Retorna False por defecto indicando que no tiene deuda
