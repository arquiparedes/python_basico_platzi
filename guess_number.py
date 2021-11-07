import random


def run():
    selected_number = 0
    random_number = random.randint(1, 100)
    message = """Bienvenido al juego Adivina el Número
    
Debe seleccionar un número entre el 1 y el 100, si adivina el número que Python escogió, usted es el ganador.

Tiene todos los intentos que desee realizar
    """
    print(message)
    selected_number = int(input("Seleccione un número: "))
    while selected_number != random_number:
        if selected_number < random_number:
            print("El número seleccionado es menor al número de Python: ")
            selected_number = int(input("Seleccione otro número: "))
        if selected_number > random_number:
            print("El número seleccionado es mayor al número de Python: ")
            selected_number = int(input("Seleccione otro número: "))
    print("Exacto, el número",str(selected_number),"es el número escogido por Python")
    print("Has Ganado!!")



if __name__ == "__main__":
    run()