def factorial(n):
    fact = n
    while n > 1:
        fact = fact*(n-1)
        n -= 1
    return fact


def is_prime_number(number):
    if number <= 0:
        print("Introduzca un número mayor o igual a 1")
    elif number == 1:
        return False
    else:
        fact = factorial(number-1)
        if (fact + 1) % number == 0:
            return True
        else:
            return False

def run():
    number = int(input("Ingrese el número que desea evaluar: "))
    if number <= 0:
        while number <= 0:
            number = int(input("El número debe ser mayor o igual a 1, ingrese el número que desea evaluar: "))
    if is_prime_number(number):
        print("El número",number,"es un número primo")
    else:
        print("El número",number,"no es un número primo")


if __name__ == "__main__":
    run()