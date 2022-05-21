# Uma função que mostra os numeros primos em um intervalo numérico 

def primos():

    inicio = int(input("Digite um numero:"))
    fim = int(input("Digite um numero:"))
    contapr = 0

    while inicio <= fim and inicio <= fim <= 5000:
        comeco = inicio
        div = 0
        cont = 1
        while cont <= comeco:
            if comeco % cont == 0:
                div += 1
            cont = cont+1
        if div == 2:
            print(comeco)
            contapr = contapr + 1
        inicio = inicio+1
    print(f'primos: {contapr}')

primos()