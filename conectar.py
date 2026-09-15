import sqlite3 # Importa el modulo estandar sqlite3 para interactuar con bases de datos SQLite
from model.marca import Marca # Importa la clase Marca desde el modulo model.marca
from model.modelo import Modelo # Importa la clase Modelo desde el modulo model.modelo
from model.auto import Auto # Importa la clase Auto desde el modulo model.auto


conexion = sqlite3.connect("taller.db") # Establece la conexion con la base de datos local SQLite taller.db

cursor = conexion.cursor() # Crea un objeto cursor para ejecutar sentencias SQL

cursor.execute("""CREATE TABLE IF NOT EXISTS Vehiculo(
             patente TEXT PRIMARY KEY,
             modelo TEXT,
             en_taller INTEGER)""") # Ejecuta la sentencia SQL para crear la tabla Vehiculo si no existe previamente
marca = Marca("Toyota") # Instancia un objeto Marca con nombre Toyota
modelo = Modelo("Yaris", marca) # Instancia un objeto Modelo con nombre Yaris y su marca asociada

auto = Auto("AB1234", 2027, modelo) # Instancia un objeto Auto con patente, anio y modelo

#cursor.execute("INSERT INTO Vehiculo (patente, modelo, en_taller) VALUES (?,?,?)",
#               (auto.patente, auto.modelo.nombre, int(auto._en_taller))) # Sentencia SQL comentada para insertar un vehiculo

cursor.execute("Select * from Vehiculo where patente = ?",("AB1234",)) # Ejecuta una consulta parametrizada para buscar el vehiculo por patente
fila = cursor.fetchone() # Obtiene la primera fila resultante de la consulta
print(fila) # Muestra por consola el registro obtenido de la base de datos

cursor.execute() # Sentencia execute adicional del codigo original

conexion.commit() # Confirma y guarda permanentemente los cambios efectuados en la base de datos
