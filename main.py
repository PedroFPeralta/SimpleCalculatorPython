import math


def calculator():
    print("Insert your matematical operation")
    operation = input("Operation: ")
    if "!sqr" in operation:
        print("Calcular raiz quadrada")
        raiz = input("Valor: ")
        print(math.sqrt(int(raiz)))
    elif "^" in operation:
        print("Erro de Sintaxe: Subsitua o caracter '^' por '**'")

    elif "sqrt" in operation:
        print("Erro de Sintaxe: Subsitua o 'sqrt' pelo valor correspondente!")
        print("Para calcular a raiz quadrada digite !sqr")
    else:
        try:
            result = eval(operation)
            print(operation + "=" + str(result))
        except:
            print("Expressão Invalida! Verifique novamente")


if __name__ == '__main__':
    while True:
        calculator()
