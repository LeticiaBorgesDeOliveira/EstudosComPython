# Função calculadora

def calculadora():
    num1 = float(input("Digite o primeiro numero:"))
    sinal = input("Digite a operação desejada:")
    num2 = float(input("Digite o segundo numero:"))

    if sinal=="+" or sinal=="-" or sinal=="*" or sinal=="/":
        if sinal=="+":
            print(f"A soma é {(num1+num2)}")
        elif sinal=="-":
            print(f"A subtração é {(num1-num2)}")
        elif sinal=="*":
            print(f"A multiplicação é {(num1*num2)}")
        elif num2>0:
            print(f"A divisão é {(num1/num2)} ")
        else:
            print("Impossivel fazer a divisão")
    else:
        print(f"{sinal} Sinal inválido")

calculadora()