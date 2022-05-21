# Função para classificar os competidores por categorias de acordo com a sua idade

def competidor():

    idade = int(input("Digite a sua idade:"))

    if idade<5:
        print("Sua categoria é Bebê")
    elif idade>=5 and idade<=7:
        print("Sua categoria é Infantil A")
    elif idade>=8 and idade<=10:
        print("sua categoria é Infantil B")
    elif idade>=11 and idade<=13:
        print("Sua categoria é Juvenil A")
    elif idade>=14 and idade<=17:
        print("Sua categoria é Juvenil B ")
    else:
        print("Sua categoria é Sênior") 

competidor()