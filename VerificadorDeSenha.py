# Função Verificadora de senha


def VerificadorSenha():

    senha = str(input("Digite a sua senha:"))

    if senha=="R10p5":
        print("Acesso Concedido")
    else:
        print("Acesso Negado")

VerificadorSenha()