# Função que cria um tabuleiro de xadrez com dois numeros dados



def tabuleiro():

    n = int(input("Digite o tamanho do tabuleiro desejado:"))
    m = int(input("Digite o tamanho do tabuleiro desejado:"))

    linha = 0
    while linha < n:
        coluna = 0
        while coluna < m:
            if (linha+coluna) % 2 == 0:
                print(2 * chr(9608), end='')
            else:
                print(2 * ' ', end='')
            coluna += 1
        print()
        linha += 1

tabuleiro()