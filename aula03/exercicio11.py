### Exercício 11. Leitura de Dados até Flag
# Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.

#Minha resolução
flag = "sair"
flag_valida = False
dados = []

while flag_valida == False:
    try:
        entrada = input("Insira uma entrada de dados (para encerrar digite 'sair'): ")
        if entrada != flag:
            dados.append(entrada)
        elif entrada == flag:
            flag_valida = True
            print(f"as entradas foram: {dados}")
            print("Programa finalizado")
    except (ValueError, TypeError):
        print("Os dados digitado são inválidos, tente novamente")


#Resolução oficial
# dados = []
# entrada = ""
# while entrada.lower() != "sair":
#     entrada = input("Digite um valor (ou 'sair' para terminar): ")
#     if entrada.lower() != "sair":
#         dados.append(entrada)
#     elif entrada.lower() == "sair":
#         print(f"As entradas foram: {dados}")
#         print("Programa finalizado")

