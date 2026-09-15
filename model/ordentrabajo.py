from model.vehiculo import Vehiculo # Importa la clase base abstracta Vehiculo desde model.vehiculo
from model.usuario import Usuario # Importa la clase Usuario desde model.usuario
from model.lineadetalle import LineaDetalle # Importa la clase LineaDetalle desde model.lineadetalle
from model.repuesto import Repuesto # Importa la clase Repuesto desde model.repuesto


class OrdenTrabajo: # Define la clase OrdenTrabajo para gestionar los trabajos del taller mecanico
    def __init__(self, numero: int, descripcion: str, vehiculo: Vehiculo, usuario: Usuario): # Constructor de la orden de trabajo
        self.__numero = numero # Asigna el numero identificador de la orden a un atributo privado
        self.__descripcion = descripcion # Asigna la descripcion del trabajo a un atributo privado
        self.__horas = 0 # Inicializa el contador de horas de mano de obra en cero como atributo privado
        self.__cerrada = False # Inicializa el estado de la orden como abierta (False) en atributo privado
        self.__vehiculo = vehiculo # Asigna la referencia al vehiculo atendido a un atributo privado
        self.__usuario = usuario # Asigna la referencia al usuario/mecanico responsable a un atributo privado
        self.__lineas_detalle = [] # Inicializa la lista de lineas de repuestos como atributo privado

    def agregar_horas(self, cantidad: int): # Metodo para registrar horas trabajadas en la orden
        if not self.__cerrada: # Valida que la orden no se encuentre cerrada antes de agregar horas
            self.__horas += cantidad # Suma la cantidad de horas especificadas a las horas acumuladas

    def agregar_repuesto(self, cantidad: int, precio_unitario: int, repuesto: Repuesto): # Metodo para anadir repuestos a la orden
        if not self.__cerrada and repuesto.hay_stock(): # Valida que la orden este abierta y que exista stock suficiente
            linea = LineaDetalle(cantidad, precio_unitario, repuesto) # Instancia una nueva linea de detalle con los datos
            self.__lineas_detalle.append(linea) # Agrega la linea a la lista de detalles de la orden
            repuesto.disminuir_stock(cantidad) # Descuenta las unidades utilizadas del inventario del repuesto

    def cerrar(self): # Metodo para dar por finalizada y cerrar la orden de trabajo
        self.__cerrada = True # Marca el estado de la orden como cerrada (True)

    def total(self) -> int: # Metodo para calcular el total a pagar de la orden de trabajo
        total_repuestos = sum(linea.subtotal() for linea in self.__lineas_detalle) # Calcula la sumatoria del subtotal de repuestos
        total_mano_obra = self.__horas * self.__vehiculo.tarifa_hora() # Calcula el costo total de mano de obra segun tarifa del vehiculo
        return total_repuestos + total_mano_obra # Retorna la suma total de repuestos y mano de obra
