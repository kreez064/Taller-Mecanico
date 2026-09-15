from model.marca import Marca # Importa la clase Marca desde el modulo model.marca


class Modelo: # Define la clase Modelo para representar el modelo de un vehiculo
    def __init__(self, nombre: str, marca: Marca): # Constructor que recibe el nombre del modelo y su marca asociada
        self.__nombre = nombre # Asigna el nombre del modelo a un atributo privado
        self.__marca = marca # Asigna la instancia de Marca asociada a un atributo privado

    @property # Decorador getter para acceder al nombre
    def nombre(self) -> str: # Metodo getter para obtener el nombre del modelo
        return self.__nombre # Retorna el valor del atributo privado __nombre

    @property # Decorador getter para acceder a la marca
    def marca(self) -> Marca: # Metodo getter para obtener el objeto Marca asociado
        return self.__marca # Retorna el valor del atributo privado __marca
