from db import SessionLocal, engine
from models import Base, Libro

# Crear tablas (si no existen)
Base.metadata.create_all(bind=engine)

#   FUNCIONES CRUD

def agregar_libro(titulo, autor, genero, estado):
    session = SessionLocal()
    try:
        libro = Libro(titulo=titulo, autor=autor, genero=genero, estado=estado)
        session.add(libro)
        session.commit()
        print(" Libro agregado correctamente.")
    except Exception as e:
        print(" Error al agregar libro:", e)
        session.rollback()
    finally:
        session.close()


def actualizar_libro(id_libro, campo, nuevo_valor):
    session = SessionLocal()
    try:
        libro = session.query(Libro).filter(Libro.id == id_libro).first()
        if not libro:
            print(" No se encontró un libro con ese ID.")
            return
        setattr(libro, campo, nuevo_valor)
        session.commit()
        print(" Libro actualizado correctamente.")
    except Exception as e:
        print(" Error al actualizar:", e)
        session.rollback()
    finally:
        session.close()


def eliminar_libro(id_libro):
    session = SessionLocal()
    try:
        libro = session.query(Libro).filter(Libro.id == id_libro).first()
        if not libro:
            print(" No se encontró un libro con ese ID.")
            return
        session.delete(libro)
        session.commit()
        print(" Libro eliminado correctamente.")
    except Exception as e:
        print(" Error al eliminar libro:", e)
        session.rollback()
    finally:
        session.close()


def ver_libros():
    session = SessionLocal()
    try:
        libros = session.query(Libro).all()
        if libros:
            print("\n LISTADO DE LIBROS:")
            for libro in libros:
                print(f"[{libro.id}] '{libro.titulo}' - {libro.autor} | Género: {libro.genero} | Estado: {libro.estado}")
        else:
            print(" No hay libros registrados.")
    finally:
        session.close()


def buscar_libros(campo, valor):
    session = SessionLocal()
    try:
        libros = session.query(Libro).filter(getattr(Libro, campo).like(f"%{valor}%")).all()
        if libros:
            print("\n RESULTADOS DE BÚSQUEDA:")
            for libro in libros:
                print(f"[{libro.id}] '{libro.titulo}' - {libro.autor} | Género: {libro.genero} | Estado: {libro.estado}")
        else:
            print(" No se encontraron coincidencias.")
    finally:
        session.close()

#   MENÚ PRINCIPAL

def menu():
    while True:
        print("\n  MENÚ BIBLIOTECA")
        print("1. Agregar nuevo libro")
        print("2. Actualizar información de un libro")
        print("3. Eliminar libro")
        print("4. Ver listado de libros")
        print("5. Buscar libros")
        print("6. Salir")

        opcion = input("Selecciona una opción (1-6): ")

        if opcion == "1":
            titulo = input("Título: ")
            autor = input("Autor: ")
            genero = input("Género: ")
            estado = input("Estado (leído / no leído): ").lower()
            if estado not in ("leído", "no leído"):
                print(" Estado inválido.")
            else:
                agregar_libro(titulo, autor, genero, estado)

        elif opcion == "2":
            ver_libros()
            id_libro = int(input("ID del libro a actualizar: "))
            campo = input("Campo a actualizar (titulo, autor, genero, estado): ").lower()
            nuevo_valor = input("Nuevo valor: ")
            actualizar_libro(id_libro, campo, nuevo_valor)

        elif opcion == "3":
            ver_libros()
            id_libro = int(input("ID del libro a eliminar: "))
            eliminar_libro(id_libro)

        elif opcion == "4":
            ver_libros()

        elif opcion == "5":
            campo = input("Buscar por (titulo, autor, genero): ").lower()
            valor = input("Valor de búsqueda: ")
            buscar_libros(campo, valor)

        elif opcion == "6":
            print(" Saliendo del programa. ¡Hasta pronto!")
            break

        else:
            print(" Opción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    menu()
