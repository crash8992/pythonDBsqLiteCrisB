from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Crear una instancia del motor de la base de datos
engine = create_engine('sqlite:///database001.db', echo=True)

# Crear una clase base declarativa
Base = declarative_base()

# Definir el modelo de tabla
class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    edad = Column(Integer)

# Crear las tablas en la base de datos
Base.metadata.create_all(engine)

# Crear una sesión
Session = sessionmaker(bind=engine)
session = Session()

def agregar_usuario():
    # Solicitar datos al usuario
    nombre = input("Ingrese el nombre del usuario: ")
    edad = int(input("Ingrese la edad del usuario: "))

    # Crear un nuevo objeto de Usuario
    nuevo_usuario = Usuario(nombre=nombre, edad=edad)

    # Agregar el objeto a la sesión y guardar en la base de datos
    session.add(nuevo_usuario)
    session.commit()
    print("Usuario agregado correctamente.")

def mostrar_usuarios():
    # Obtener todos los usuarios de la base de datos
    usuarios = session.query(Usuario).all()

    # Mostrar los usuarios
    print("Usuarios:")
    for usuario in usuarios:
        print(f"ID: {usuario.id}, Nombre: {usuario.nombre}, Edad: {usuario.edad}")

def main():
    while True:
        # Solicitar la operación al usuario
        print("¿Qué operación deseas realizar?")
        print("1. Agregar usuario")
        print("2. Mostrar usuarios")
        print("3. Salir")
        opcion = input("Opción: ")

        if opcion == "1":
            agregar_usuario()

        elif opcion == "2":
            mostrar_usuarios()

        elif opcion == "3":
            break

        else:
            print("Opción no válida. Inténtalo nuevamente.")

if __name__ == "__main__":
    main()


