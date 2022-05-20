# Gera um triangulo retangulo com as letras do alfabeto

def triangulo():

    vezes = int(input("Digite um número de 1 a 26: "))
    alfabeto = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

    for i in range(vezes):
        print(alfabeto[i]*(i+1))

triangulo()