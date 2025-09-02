### Exercício 12. Validação de Entrada
# Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.

range_nota = list(range(1,11))
range_valido = False


while range_valido == False:
    try:
        nota = int(input("Insira uma nota para o app (de 1 a 10): "))
        if nota in range_nota:
            range_valido = True
            print(f"Sua nota dada foi {nota}")
        else:
            print("Digite uma nota de 1 a 10")
    except (ValueError, TypeError):
        print("O tipo de dados digitado não é um número inteiro.")