#Escreva um programa em Python que solicita ao usuário para digitar seu nome, o valor do seu salário mensal 
# e o valor do bônus que recebeu. O programa deve, então, 
# imprimir uma mensagem saudando o usuário pelo nome e informando o valor do salário em comparação com o bônus recebido.

nome = input("Digite seu nome: ")
salario = float(input("Digite seu salário: "))
perc_bonus = float(input("Digite o percentual de bônus recebido: "))
kpi_bonus_2024 = 1000 

bonus_2024 = kpi_bonus_2024 + salario * (perc_bonus / 100)


print(f"Olá {nome}, o seu valor de bônus foi de R${bonus_2024}.")