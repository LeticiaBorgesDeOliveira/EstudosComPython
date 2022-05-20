# Função que faz o calculo do desconto do INSS do salario do colaborador de acordo com o valor do salario

def descontoINSS():

    salario = float(input("Digite seu Salario Bruto:"))

    if salario<=600:
        print("Não é cobrado inss do seu salário.")
    elif salario>600 and salario<1200:
        print(f'Valor de INSS descontado do seu salario será: {(salario*20)/100}')
    elif salario>1200 and salario<=2000:
        print(f'Valor de INSS descontado do seu salario será: {(salario*25)/100}')
    elif salario>2000:
        print(f'Valor de INSS descontado do seu salario será: {(salario*30)/100}')

descontoINSS()
