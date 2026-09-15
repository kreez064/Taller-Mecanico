from model.vehiculo import Vehiculo # Importa la clase base abstracta Vehiculo desde model.vehiculo
from model.modelo import Modelo # Importa la clase Modelo desde model.modelo


class Auto(Vehiculo): # Define la clase Auto que hereda de la clase abstracta Vehiculo
    def __init__(self, patente: str, anio: int, modelo: Modelo): # Constructor de Auto que recibe patente, anio y modelo
        super().__init__(patente, anio, modelo) # Invoca al constructor de la clase base Vehiculo

    def tarifa_hora(self) -> int: # Implementa el metodo abstracto tarifa_hora especifico para Auto
        return 25000 # Retorna el valor fijo de tarifa por hora para auto ($25.000)
