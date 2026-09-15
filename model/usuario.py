from model.rol import Rol # Importa la clase Rol desde el modulo model.rol
from model.persona import Persona # Importa la clase Persona desde el modulo model.persona


class Usuario: # Define la clase Usuario para la autenticacion y control de acceso al sistema
    def __init__(self, usuario: str, password_hash: str, rol: Rol, persona: Persona): # Constructor que inicializa los datos del usuario
        self.__usuario = usuario # Asigna el nombre de usuario a un atributo privado
        self.__password_hash = password_hash # Asigna el hash de la contrasena a un atributo privado
        self.__rol = rol # Asigna el rol asociado a un atributo privado
        self.__persona = persona # Asigna los datos personales (Persona) a un atributo privado

    def autenticar(self, password_hash: str) -> bool: # Metodo para autenticar al usuario comparando el hash de la contrasena
        return self.__password_hash == password_hash # Retorna True si el hash coincide con el almacenado

    def puede(self, accion: str) -> bool: # Metodo para validar si el usuario tiene permiso para ejecutar una accion
        return self.__rol.tiene_permiso(accion) # Delega la validacion al metodo tiene_permiso del rol
