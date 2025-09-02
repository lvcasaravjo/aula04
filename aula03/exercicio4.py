### Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação, 
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha 
# fornecido um email válido. Escreva um programa que valide essas condições 
# e imprima "Dados de usuário válidos" ou o erro específico encontrado.

idade_valida = False
email_valido = False

while idade_valida == False:
    try:
        idade = int(input('Insira a sua idade: '))
        if idade < 18 and idade > 65:
            raise ValueError("Você não possui a idade adequada para se cadastrar.")
        else:
            idade_valida = True
    except (ValueError, TypeError):
        print("Os dados digitado são inválidos, tente novamente")


while email_valido == False:
    try:
        email = input("Digite um e-mail válido: ")
        if len(email) < 10:
            raise ValueError("Você digitou um e-mail inválido.")
        elif email.isdigit():
            raise ValueError("Você digitou um e-mail inválido.")
        elif email.isspace():
            raise ValueError("Você digitou um e-mail inválido.")
        else:
            email_valido = True
            print("Dados de usuário válidos.")
    except (ValueError, TypeError):
        print("Os dados digitado são inválidos, tente novamente")

