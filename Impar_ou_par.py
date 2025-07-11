print("==============================")
print("Descubra se é par ou impar")
print("para finalizar escreva:'Fim'")
print("==============================")

def Funcao():
    while True:
        pergunta = input("qual o numero:")

        if pergunta.lower() == "fim":
            break

        try:
            numero = int(pergunta)
            if (numero % 2) == 0:
                print(f"{numero} é um número par")
            else:
                print(f"{numero} é um número impar")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número ou 'Fim'.")

Funcao()