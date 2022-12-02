
import sqlite3 # Importamos el modulo
# Conexion a la DB
#conexion(variable, canal para comunicar la bd)
#utilizamos el modulo "slite3"
#connect(metodo de conexion)
conexion = sqlite3.connect('supermarket.db')
#conexion.close() # Cerramos la conexion

#cursor= objeto(creo que es variable ) que maneja las consultas, se encarga de ejecutar las sentencias sql
cursor= conexion.cursor()

#usamos el objeto cursor + el metodo ejecutar
#cursor.execute("INSERT INTO Persona VALUES(joaquin, tejerina, 4368756,cliente)")
#conexion.close()

cursor.execute("INSERT INTO Persona VALUES( 2,'Hector','valdivia',30456783,'cliente')")

conexion.commit()



#resultado= variable donde se guarda el metodo de consulta(respuesta a la consulta execute)
#resultado = cursor.execute("SELECT nombre,apellido,dni FROM Persona")

#filas= resultado.fetchone()

#print(filas )