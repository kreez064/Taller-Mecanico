class Rol: # Define la clase Rol para gestionar los roles y permisos del sistema
    def __init__(self, nombre: str, permisos: list): # Constructor que recibe el nombre del rol y una lista de permisos
        self.__nombre = nombre # Asigna el nombre del rol a un atributo privado
        self.__permisos = permisos # Asigna la lista de permisos a un atributo privado

    def tiene_permiso(self, accion: str) -> bool: # Metodo para comprobar si el rol posee un permiso especifico
        return accion in self.__permisos # Retorna True si la accion esta en la lista de permisos, False en caso contrario
