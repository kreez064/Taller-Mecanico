from model.repuesto import Repuesto # Importa la clase Repuesto desde el modulo model.repuesto


class LineaDetalle: # Define la clase LineaDetalle para representar un item de repuesto dentro de una orden
    def __init__(self, cantidad: int, precio_unitario: int, repuesto: Repuesto): # Constructor con cantidad, precio y repuesto
        self.__cantidad = cantidad # Asigna la cantidad solicitada a un atributo privado
        self.__precio_unitario = precio_unitario # Asigna el precio unitario a un atributo privado
        self.__repuesto = repuesto # Asigna la referencia al objeto Repuesto a un atributo privado

    def subtotal(self) -> int: # Metodo para calcular el subtotal de la linea de detalle
        return self.__cantidad * self.__precio_unitario # Multiplica la cantidad por el precio unitario y retorna el resultado
