from colorama import init
from termcolor import colored

init()
col_disp = {-1: True, 1: True, 2: True, 3: True, 4: True, 5: True, 6: True, 7: True}
color = 1
colores = {1: "red", 2: "blue", 3: "green", 4: "magenta",
           5: "white", 6: "cyan", 7: "yellow", -1: "grey"}
print(colored("CRIBA DE ERASTÓTENES\n", colores[1]).center(80, " "))


def ObtenerNumero():
    while True:
        numero = input('Escriba un número natural mayor a dos: ')
        try:
            val = int(numero)
            if val <= 2:
                raise ValueError
            break
        except ValueError:
            print("Escriba un número natural válido")
    return val


def CalcularNumeros(num):
    numeros_colores = {}
    for i in range(2, num + 1):
        numeros_colores[i] = colores[5]
    return numeros_colores


def CalcularPrimos(n_col, next_index=2):
    color = BuscarPorValor(col_disp, True)
    col_disp[color] = False
    for i, v in n_col.items():
        if i == next_index:
            n_col[i] = colores[3]
        if i % next_index == 0 and n_col[i] != colores[3]:
            n_col[i] = colores[color]
    return n_col


def BuscarPorValor(n_col, text):
    result = -1
    for key, value in n_col.items():
        if value == text:
            return key
    return result


def ImprimirNumeros(n_col, numero):
    for i, v in n_col.items():
        print('{: <12}'.format(colored(i, v)), end='| ')
        if i % 15 == 0:
            print()
    print(f"\nNúmeros primos en el rango 2 y {numero}")
    for i, v in n_col.items():
        if v == colores[3]:
            print(i, end=' ,')
            if i % 6 == 0:
                print()


numero = ObtenerNumero()
numeros_colores = CalcularNumeros(numero)
numeros_colores = CalcularPrimos(numeros_colores)

while BuscarPorValor(numeros_colores, colores[5]) > 0:
    next_index = BuscarPorValor(numeros_colores, colores[5])
    numeros_colores = CalcularPrimos(numeros_colores, next_index)

ImprimirNumeros(numeros_colores, numero)
