# Função que organiza a sequencia dos numeros de forma decrescente

def Crescente():

    num1 = float(input("Digite o primeiro numero:"))
    num2 = float(input("Digite o segundo numero:"))

    if num1>num2:
        print(num1,num2, sep=(","))
    else:
        print(num2,num1, sep=(","))

Crescente()