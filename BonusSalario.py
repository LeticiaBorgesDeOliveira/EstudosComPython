# Função que fala quanto de bonus o funcionario vai ganhar de acordo com o salario e os anos de empresa

def bonus():

    salario =float(input("Insira o valor do salario:")) 
    anos = int(input("Insira a quantidade de anos que voce trabalha na empresa:"))
    
    if anos>=5:
        print("Voce ganhará um bonus de:", float((salario*20)/100))
    else:
        print("Você ganhará um bonus de:", float((salario*10)/100))

bonus()

