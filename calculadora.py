#algoritmo:calculadora

def adicionar(num1,num2):
    return num1 + num2

def subtrair(num1,num2):
    return num1 - num2

def multiplicar(num1,num2):
    return num1 * num2

def divisao(num1,num2):
    return num1 / num2

    if num2 == 0:
        return "Erro: Não existe divisao por zero"

        return num1 / num2

def calculadora():
    while True:
        try:
            num1 = float(input("qual o primeiro numero:"))
            num2 = float(input("qual o segundo numero:"))
            operacao = input("Digite qual a operação(+,-,*,/):")

            if operacao == "+":
                resultado = adicionar(num1, num2)
            elif operacao == "-":
                resultado = subtrair(num1, num2)
            elif operacao == "*":
                resultado = multiplicar(num1, num2)
            elif operacao == "/":
                resultado = divisao(num1, num2)
            else:
                resultado = "operação invalida"

            print("Resultado:", resultado)
        except ValueError:
            print("entrada invalida. Digite numeros")

calculadora()
