#Função que verifica se os numeros são iguais, e caso nao sejam, ele subtrai um pelo outro mostrando a diferença



def igualdade():
    num1 =int(input("Digite o primeiro numero inteiro:"))
    num2 =int(input("Digite o segundo numero Inteiro:"))
    
    if num1 == num2:
        print("Numeros Iguais")
    else:
        if num1>num2:
            print("A diferença é:", num1-num2 )
        else:
            print("A diferença é:", num2-num1)

igualdade()




