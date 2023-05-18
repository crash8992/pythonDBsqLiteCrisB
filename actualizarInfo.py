from dataBaseCB import conn

cursor = conn.cursor()

nombre = input("INTRODUCE NOMBRE: ")
apellido = input("INTRODUCE APELLIDO: ")
cedula = int(input("INGRESE LA CEDULA: "))
edad = int(input("INGRESE LA EDAD: "))

cadena_sql = """INSERT INTO Autor (nombre, apellido, cedula, edad) \
VALUES ('%s', '%s', '%s', %d);""" % (nombre, apellido, cedula, edad)
cursor.execute(cadena_sql)

conn.commit()

cadena_consulta_sql = "SELECT * from Autor"
cursor.execute(cadena_consulta_sql)

informacion = cursor.fetchall()

for d in informacion:
    print("%s - %s - %s - %d" % (d[0], d[1], d[2], d[3]))
    
print("------------------------")

cursor.close()