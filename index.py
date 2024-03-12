import math

def soma(a, b):
    return a + b

def sub(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    return a / b

def raiz(a):
    return (round(math.sqrt(a), 2))

def calculadora():
    operador = input("Informe o operador \n + - Adição \n (-) - Subtração \n * - Multiplicação \n / - Divisão \n R - Raiz ")

    if operador == "R":
      num1 = float(input("Informe seu numero: "))
      resultado = raiz(num1)
      print("O Resultado é", resultado)
    else:
        num1 = int(input("Informe seu 1° numero: "))
        num2 = int(input("Informe seu 2° numero: "))
        if operador == "-":
            resultado = sub(num1, num2)
            print("O resultado é", resultado)
        elif operador == "+":
            resultado = soma(num1, num2)
            print("O resultado é", resultado)
        elif operador == "/":
            resultado = div(num1, num2)
            print("O resultado é", resultado)
        elif operador == "*":
            resultado = mult(num1, num2)
            print("O resultado é", resultado)
        else:
            print("Operação inválida")

calculadora()
        