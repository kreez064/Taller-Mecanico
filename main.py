from model.marca import Marca # Importa la clase Marca desde el modulo model.marca
from model.modelo import Modelo # Importa la clase Modelo desde el modulo model.modelo
from model.auto import Auto # Importa la clase Auto desde el modulo model.auto
from model.moto import Moto # Importa la clase Moto desde el modulo model.moto
from model.camion import Camion # Importa la clase Camion desde el modulo model.camion
from model.persona import Persona # Importa la clase Persona desde el modulo model.persona
from model.cliente import Cliente # Importa la clase Cliente desde el modulo model.cliente
from model.rol import Rol # Importa la clase Rol desde el modulo model.rol
from model.usuario import Usuario # Importa la clase Usuario desde el modulo model.usuario
from model.repuesto import Repuesto # Importa la clase Repuesto desde el modulo model.repuesto
from model.ordentrabajo import OrdenTrabajo # Importa la clase OrdenTrabajo desde el modulo model.ordentrabajo


def main(): # Funcion principal para ejecutar las pruebas del taller mecanico
    # 1. Crear Marcas y Modelos
    marca_toyota = Marca("Toyota") # Instancia la marca Toyota
    modelo_yaris = Modelo("Yaris", marca_toyota) # Instancia el modelo Yaris asociado a la marca Toyota

    marca_honda = Marca("Honda") # Instancia la marca Honda
    modelo_cbr = Modelo("CBR500R", marca_honda) # Instancia el modelo CBR500R asociado a la marca Honda

    marca_volvo = Marca("Volvo") # Instancia la marca Volvo
    modelo_fh = Modelo("FH16", marca_volvo) # Instancia el modelo FH16 asociado a la marca Volvo

    # 2. Instanciar Vehiculos
    auto = Auto("AB1234", 2018, modelo_yaris) # Instancia un vehiculo de tipo Auto con su patente, anio y modelo
    moto = Moto("CD5678", 2020, modelo_cbr) # Instancia un vehiculo de tipo Moto con su patente, anio y modelo
    camion = Camion("EF9012", 2023, modelo_fh, 5000) # Instancia un vehiculo de tipo Camion con su patente, anio, modelo y capacidad de carga

    # 3. Pruebas de ingreso al taller
    print("--- Ingreso de Vehículos ---") # Imprime encabezado de seccion de ingreso de vehiculos
    print(auto.ingresar()) # Registra el ingreso del auto y muestra el resultado por consola
    print(moto.ingresar()) # Registra el ingreso de la moto y muestra el resultado por consola
    print(camion.ingresar()) # Registra el ingreso del camion y muestra el resultado por consola
    print() # Imprime una linea en blanco para separar secciones

    # 4. Pruebas de tarifas
    print("--- Tarifas por Hora ---") # Imprime encabezado de seccion de tarifas
    print(f"Tarifa Auto ({auto.modelo.marca.nombre} {auto.modelo.nombre}): ${auto.tarifa_hora()}") # Muestra la tarifa por hora calculada para el auto
    print(f"Tarifa Moto ({moto.modelo.marca.nombre} {moto.modelo.nombre}): ${moto.tarifa_hora()}") # Muestra la tarifa por hora calculada para la moto
    print(f"Tarifa Camión ({camion.modelo.marca.nombre} {camion.modelo.nombre}): ${camion.tarifa_hora()}") # Muestra la tarifa por hora calculada para el camion
    print() # Imprime una linea en blanco para separar secciones

    # 5. Crear Personas, Clientes y Usuarios
    persona_mecanico = Persona("12.345.678-9", "Juan Mecánico") # Instancia los datos personales del mecanico
    rol_mecanico = Rol("Mecánico", ["reparar", "cerrar_orden"]) # Instancia el rol Mecanico con sus permisos asignados
    usuario_mecanico = Usuario("juanm", "hash123", rol_mecanico, persona_mecanico) # Instancia el usuario del mecanico para autenticacion

    persona_cliente = Persona("9.876.543-2", "Pedro Cliente") # Instancia los datos personales del cliente
    cliente_pedro = Cliente(persona_cliente) # Instancia el cliente asociando su informacion de persona

    # 6. Crear Orden de Trabajo
    print("--- Gestión de Orden de Trabajo ---") # Imprime encabezado de seccion de orden de trabajo
    orden1 = OrdenTrabajo(1, "Cambio de aceite y pastillas", auto, usuario_mecanico) # Instancia una nueva orden de trabajo para el auto
    orden1.agregar_horas(3) # Registra 3 horas de mano de obra en la orden
    
    # 7. Agregar Repuestos
    filtro = Repuesto("F-001", "Filtro de Aceite", 10, False) # Instancia un repuesto de filtro de aceite con stock de 10 unidades
    pastillas = Repuesto("P-002", "Pastillas de freno", 5, True) # Instancia un repuesto de pastillas de freno con stock de 5 unidades
    
    orden1.agregar_repuesto(1, 15000, filtro) # Agrega 1 unidad de filtro a la orden con precio unitario de $15.000
    orden1.agregar_repuesto(1, 45000, pastillas) # Agrega 1 unidad de pastillas a la orden con precio unitario de $45.000
    
    # 8. Calcular Total y Cerrar
    print(f"Total de Orden #1 (Mano de obra + Repuestos): ${orden1.total()}") # Calcula e imprime el monto total acumulado de la orden
    orden1.cerrar() # Cierra formalmente la orden de trabajo impidiendo modificaciones posteriores
    print("Orden cerrada exitosamente.") # Muestra mensaje de confirmacion de cierre


if __name__ == "__main__": # Verifica si el script se esta ejecutando directamente como archivo principal
    main() # Invoca a la funcion principal para iniciar la ejecucion del programa
