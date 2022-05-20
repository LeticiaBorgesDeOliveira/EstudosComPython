# Uma Função que mostra quantos e quais são os anos bissextos de um intervalo de anos.

def anobissexto():

    ano_inicio = int(input("Digite o ano: "))
    ano_fim = int(input("Digite o ano final: "))

    contagem = 0

    for ano in range(ano_inicio+1, ano_fim + 1):
        if ano % 4 == 0:
            print(ano)
            contagem += 1
      
    print(f"Bissextos: {contagem}")

anobissexto()