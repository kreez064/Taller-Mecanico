from model.vehiculo import Vehiculo # Importa la clase base abstracta Vehiculo desde model.vehiculo
from model.modelo import Modelo # Importa la clase Modelo desde model.modelo


class Camion(Vehiculo): # Define la clase Camion que hereda de la clase abstracta Vehiculo
    def __init__(self, patente: str, anio: int, modelo: Modelo, capacidad_carga: int): # Constructor con patente, anio, modelo y capacidad de carga
        super().__init__(patente, anio, modelo) # Invoca al constructor de la clase base Vehiculo
        self.__capacidad_carga: int = capacidad_carga # Guarda la capacidad de carga en kilos como atributo privado

    def tarifa_hora(self) -> int: # Implementa el metodo abstracto tarifa_hora especifico para Camion
        return 40000 # Retorna el valor fijo de tarifa por hora para camion ($40.000)
