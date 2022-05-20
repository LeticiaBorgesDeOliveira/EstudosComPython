# Função que verifica se o numero digitado está dentro do intervalo entre 50 e 100


def verificador():
    
    num = int(input("Digite um numero Inteiro:"))

    if num >=50 and num <=100 :
        print(f'{num}, Pertence ao intervalo')
    else:
        print(f'{num},"Nao pertence ao intervalo')

verificador()