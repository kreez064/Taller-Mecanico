class Persona: # Define la clase Persona para representar a una persona con RUT y nombre
    def __init__(self, rut: str, nombre: str): # Constructor que recibe el RUT y el nombre de la persona
        self.__rut = rut # Asigna el RUT a un atributo privado
        self.__nombre = nombre # Asigna el nombre a un atributo privado

    @property # Decorador getter para acceder al RUT
    def rut(self) -> str: # Metodo getter para obtener el RUT de la persona
        return self.__rut # Retorna el valor del atributo privado __rut

    @property # Decorador getter para acceder al nombre
    def nombre(self) -> str: # Metodo getter para obtener el nombre de la persona
        return self.__nombre # Retorna el valor del atributo privado __nombre
