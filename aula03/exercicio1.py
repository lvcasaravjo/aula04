### Exercício 1: Verificação de Qualidade de Dados
# Você está analisando um conjunto de dados de vendas e precisa garantir 
# que todos os registros tenham valores positivos para `quantidade` e `preço`. 
# Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos 
# forem positivos ou "Dados inválidos" caso contrário.

quantidade_valida = False
preco_valido = False

while quantidade_valida == False and preco_valido == False:
    try:
        quantidade = int(input('Insira a quantidade: '))
        preco = float(input('Digite o preço: '))
        if quantidade <= 0 or preco <= 0:
            raise ValueError("Os dados digitado são inválidos, tente novamente")
        else:
            quantidade_valida = True
            preco_valido = True
            print('Dados válidos')
    except (ValueError, TypeError):
        print("Os dados digitado são inválidos, tente novamente")