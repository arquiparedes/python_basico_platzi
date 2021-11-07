import random


# Repetir programa
def repeat_program(func, name):
    repeat = "s"
    while repeat == "s":
        func()
        repeat = input("\nSi desea " + name + ", presione S y ENTER, de lo contrario solo presione ENTER\n")
        repeat = repeat.lower()


# Money converter functions
def money_option(money_type,money_value):
    money = input("\nCuantos " + money_type + " desea convertir a dolares americanos? ")
    money = float(money)
    dollars = money/money_value
    dollars = round(dollars,2)
    dollars = str(dollars)
    print("\nEsto equivale a " + dollars + " dolares americanos")


def money_converter():
    converter_menu = """
Bienvenidos al conversor de monedas a Dolares Americanos.

1. Pesos Colombianos
2. Pesos Argentinos
3. Pesos Mexicanos

Elija una opción: """

    money_menu = int(input(converter_menu))

    if money_menu == 1:
        money_option("Pesos Colombianos", 3799)
    if money_menu == 2:
        money_option("Pesos Argentinos", 99.83)
    if money_menu == 3:
        money_option("Pesos Mexicanos", 20.79)


# Palindrome functions
def palindrome():
    word = input("\nIntroduzca un Palindromo: ")
    palindrome = word.lower()
    palindrome = palindrome.replace(" " , "")
    reverse_palindrome = palindrome[::-1]

    if palindrome == reverse_palindrome:
        print("\nSu busqueda: " + word + ", sí es un palíndromo")
    else:
        print("\nSu busqueda: " + word + ", no es un palíndromo")


# Prime numbers
def factorial(n):
    fact = n
    while n > 1:
        fact = fact*(n-1)
        n -= 1
    return fact


def is_prime_number(number):
    if number <= 0:
        print("\nIntroduzca un número mayor o igual a 1")
    elif number == 1:
        return False
    else:
        fact = factorial(number-1)
        if (fact + 1) % number == 0:
            return True
        else:
            return False


def prime_numbers():
    number = int(input("\nIngrese el número que desea evaluar: "))
    if number <= 0:
        while number <= 0:
            number = int(input("\nEl número debe ser mayor o igual a 1, ingrese el número que desea evaluar: "))
    if is_prime_number(number):
        print("\nEl número",number,"sí es un número primo")
    else:
        print("\nEl número",number,"no es un número primo")


# Guess the Number functions
def guess_number():
    selected_number = 0
    random_number = random.randint(1, 100)
    message = """Bienvenido al juego Adivina el Número
    
Debe seleccionar un número entre el 1 y el 100, si adivina el número que Python escogió, usted es el ganador.

Tiene todos los intentos que desee realizar
    """
    print(message)
    selected_number = int(input("\nSeleccione un número: "))
    while selected_number != random_number:
        if selected_number < random_number:
            print("\nEl número seleccionado es menor al número de Python: ")
            selected_number = int(input("\nSeleccione otro número: "))
        if selected_number > random_number:
            print("\nEl número seleccionado es mayor al número de Python: ")
            selected_number = int(input("\nSeleccione otro número: "))
    print("\nExacto, el número",str(selected_number),"es el número escogido por Python")
    print("\nHas Ganado!!")


# Generador de Contraseñas
def pass_gen():
    MAYUS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
    MINUS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
    NUMS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    CHARS = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '&', '$', '#', '"']

    characters = MAYUS + MINUS + NUMS + CHARS
    password = []

    for i in range (15):
        character = random.choice(characters)
        password.append(character)

    password = "".join(password)
    print("\nTu contraseña es", password)


def run():
    welcome = """Bienvenidos, en este programa podrá ver el resultado de los diferenetes proyectos realizados en el curso básico de Python de Platzi.

Escoja del siguiente menú que proyecto quiere probar:

1. Conversor de Dinero
2. Palíndromos
3. Números Primos
4. Adivina el número
5. Generador de Contraseñas
6. Salir
"""
    menu = 0

    while menu != 6:

        menu = int(input(welcome))

        if menu == 1:
            repeat_program(money_converter,"utilizar el conversor de monedas nuevamente")

        if menu == 2:
            repeat_program(palindrome,"buscar otro palíndromo")

        if menu == 3:
            repeat_program(prime_numbers,"evaluar otro número")

        if menu == 4:
            repeat_program(guess_number,"jugar nuevamente")

        if menu == 5:
            repeat_program(pass_gen,"generar otra contraseña")

        if menu < 1 or menu > 6:
            print("\n" ,"Introduzco un número válido, entre 1 y 6", "\n")
            

if __name__ == "__main__":
    run()