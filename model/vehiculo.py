from abc import ABC, abstractmethod # Importa ABC y abstractmethod para definir una clase abstracta
from model.modelo import Modelo # Importa la clase Modelo desde el modulo model.modelo


class Vehiculo(ABC): # Define la clase abstracta Vehiculo que sirve como base para todos los tipos de vehiculos
    def __init__(self, patente: str, anio: int, modelo: Modelo): # Constructor base que recibe patente, anio y modelo
        self.patente = patente # Asigna la patente a traves del setter para ejecutar la validacion
        self.__anio: int = anio # Asigna el anio del vehiculo a un atributo privado
        self._en_taller: bool = False # Inicializa el estado en taller como False (protegido)
        self.__modelo: Modelo = modelo # Asigna el objeto Modelo a un atributo privado

    @property # Decorador getter para la patente
    def patente(self) -> str: # Metodo getter para obtener la patente del vehiculo
        return self.__patente # Retorna el valor del atributo privado __patente

    @patente.setter # Decorador setter para validar y asignar la patente
    def patente(self, valor: str) -> None: # Metodo setter que intercepta y valida la patente asignada
        if len(valor) < 6 or " " in valor: # Valida que tenga al menos 6 caracteres y no contenga espacios
            raise ValueError("La patente debe tener al menos 6 caracteres y no debe contener espacios.") # Lanza error si no cumple el formato
        self.__patente = valor # Asigna el valor validado al atributo privado __patente

    @property # Decorador getter para el modelo
    def modelo(self) -> Modelo: # Metodo getter para acceder al objeto Modelo
        return self.__modelo # Retorna el objeto Modelo almacenado en el atributo privado __modelo

    def ingresar(self) -> str: # Metodo para registrar el ingreso del vehiculo al taller
        if self._en_taller: # Comprueba si el vehiculo ya se encuentra dentro del taller
            return "El vehículo ya se encuentra en el taller." # Retorna mensaje informativo si ya estaba dentro
        self._en_taller = True # Cambia el estado a True indicando que esta dentro del taller
        return "El vehículo ha ingresado al taller." # Retorna mensaje de confirmacion de ingreso

    def entregar(self) -> str: # Metodo para registrar la entrega y salida del vehiculo del taller
        if not self._en_taller: # Comprueba si el vehiculo no se encuentra actualmente en el taller
            return "El vehículo no se encuentra en el taller." # Retorna mensaje informativo si no estaba dentro
        self._en_taller = False # Cambia el estado a False indicando que salio del taller
        return "El vehículo ha sido entregado." # Retorna mensaje de confirmacion de entrega

    @abstractmethod # Decorador que define el metodo como abstracto (debe ser implementado por las subclases)
    def tarifa_hora(self) -> int: # Metodo abstracto para obtener la tarifa por hora segun el tipo de vehiculo
        pass # Deja el metodo sin implementacion en la clase base abstracta
