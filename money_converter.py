def money_option(money_type,money_value):
    print("")
    money = input("Cuantos " + money_type + " desea convertir a dolares americanos? ")
    money = float(money)
    dollars = money/money_value
    dollars = round(dollars,2)
    dollars = str(dollars)
    print("")
    print("Esto equivale a " + dollars + " dolares americanos")

def run():
    menu = """
Bienvenidos al conversor de monedas a Dolares Americanos.

1. Pesos Colombianos
2. Pesos Argentinos
3. Pesos Mexicanos

Elija una opción: """

    menu = int(input(menu))

    if menu == 1:
        money_option("Pesos Colombianos", 3799)
    if menu == 2:
        money_option("Pesos Argentinos", 99.83)
    if menu == 3:
        money_option("Pesos Mexicanos", 20.79)

if __name__ == "__main__":
    run()