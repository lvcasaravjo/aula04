# Integre na solução anterior um fluxo de While 
# que repita o fluxo até que o usuário insira as 
# informações corretas

nome_valido = False
salario_valido = False
bonus_valido = False

while nome_valido is not True: 
    try:
        nome = input("Digite seu nome: ")
        if len(nome) == 0:
            raise ValueError("O nome não pode estar vazio.")
        elif any(char.isdigit() for char in nome):
            raise ValueError("O nome não deve conter números.")
        elif nome.isspace():
            raise ValueError("Você digitou apenas espaços em branco")
        else:
            nome_valido = True
            print(f"Nome válido: {nome}")
    except ValueError as e:
        print(e)

while salario_valido is not True: 
    try:
        salario = float(input("Digite o valor do seu salário: "))
        if salario < 0:
            print("Por favor, digite um valor positivo para o salário.")
        else: 
            salario_valido = True
            print(f"Salário válido: {salario}")
    except ValueError:
        print("Entrada inválida para o salário. Por favor, digite um número.")

while bonus_valido is not True:
    try:
        bonus_recebido = float(input("Digite o valor do bônus recebido: "))
        if bonus_recebido < 0:
            print("Por favor, digite um valor positivo para o bônus.")
        else: 
            bonus_valido = True
            print(f"Salário válido: {bonus_recebido}")
    except ValueError:
        print("Entrada inválida para o bônus. Por favor, digite um número.")

bonus_final = bonus_recebido * 1.2  
kpi = (salario + bonus_final) / 1000  

print(f"Seu KPI é: {kpi:.2f}")
print(f"{nome}, seu salário é R${salario:.2f} e seu bônus final é R${bonus_final:.2f}.")