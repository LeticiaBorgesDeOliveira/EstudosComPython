# Função divisora que aceita apenas numeros maiores ou iguais a 20 

def divisor():

    num = int(input("Digite um numero inteiro:"))

    if num >=20 :

        print(f"A divisao deste numero por dois é: {num/2}" )
    else:
        print("Numero invalido tente novamente")

divisor()