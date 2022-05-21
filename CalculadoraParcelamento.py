# funlçao calculadora de parcelamento de acordo com o salario

def parcelamento():

    salario = float(input("Digite seu salario bruto:")) 
    valor = float(input("Digite o valor da prestação desejada:"))

    if valor>=(salario*0.3):
        print("Valor nao aceito")
    elif valor<(salario*0.3):
        print("Valor aceito")

parcelamento()

