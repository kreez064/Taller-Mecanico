class Repuesto: # Define la clase Repuesto para representar las piezas y repuestos del taller
    def __init__(self, codigo: str, nombre: str, stock: int, es_importado: bool): # Constructor que inicializa los atributos del repuesto
        self.__codigo = codigo # Asigna el codigo del repuesto a un atributo privado
        self.__nombre = nombre # Asigna el nombre del repuesto a un atributo privado
        self.__stock = stock # Asigna la cantidad disponible en inventario a un atributo privado
        self.__es_importado = es_importado # Asigna si el repuesto es importado o nacional como booleano privado

    def hay_stock(self) -> bool: # Metodo para consultar si existen unidades disponibles en stock
        return self.__stock > 0 # Retorna True si el stock es mayor a cero

    def disminuir_stock(self, cantidad: int): # Metodo para rebajar unidades del inventario
        if self.__stock >= cantidad: # Valida que haya suficiente stock disponible para descontar
            self.__stock -= cantidad # Resta la cantidad especificada del stock actual
