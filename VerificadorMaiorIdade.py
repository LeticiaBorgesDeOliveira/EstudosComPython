# Função verificadora de idade


def maioridade():
    
    idade = int(input("Insira a sua idade:"))

    if idade>=18:
        print("Você é maior de idade")
    else:
        print("Você é menor de idade")

maioridade()