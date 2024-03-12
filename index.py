import math

def calculadora():
    operador = input("Informe o operador \n + - Adição \n (-) - Subtração \n * - Multiplicação \n / - Divisão \n R - Raiz ")

    if operador == "R":
      num1 = float(input("Informe seu numero: "))
      resultado = round(math.sqrt(num1), 2)
      print("O Resultado é", resultado)
    else:
        num1 = int(input("Informe seu 1° numero: "))
        num2 = int(input("Informe seu 2° numero: "))
        if operador == "-":
            resultado = num1 - num2
            print("O resultado é", resultado)
        elif operador == "+":
            resultado = num1 + num2
            print("O resultado é", resultado)
        elif operador == "/":
            resultado = num1 / num2
            print("O resultado é", resultado)
        elif operador == "*":
            resultado = num1 * num2   
            print("O resultado é", resultado)
        else:
            print("Operação inválida")

calculadora()
        