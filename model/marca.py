class Marca: # Define la clase Marca para representar marcas de vehiculos
    def __init__(self, nombre: str): # Constructor que recibe el nombre de la marca
        self.__nombre = nombre # Asigna el nombre a un atributo privado

    @property # Decorador getter para acceder al nombre
    def nombre(self) -> str: # Metodo getter para obtener el nombre de la marca
        return self.__nombre # Retorna el valor del atributo privado __nombre
