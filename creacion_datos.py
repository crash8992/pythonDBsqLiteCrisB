from dataBaseCB import conn

cursor = conn.cursor()

cadena_sql =  'CREATE TABLE Autor (nombre TEXT, apellido TEXT, cedula TEXT, \
            edad INTEGER)'


cursor.execute(cadena_sql)

cursor.close()