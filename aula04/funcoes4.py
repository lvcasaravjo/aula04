# Implemente uma função que receba dois argumentos: uma lista de números e um número. 
# A função deve retornar todas as combinações de pares na lista que somem ao número dado.

def soma_n_par(lista: list, numero: int) -> list:
    pares = []
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] + lista[j] == numero:
                pares.append((lista[i], lista[j]))
    return pares

# Exemplo de uso:
lista_ini = [2, 5, 3, 8, 7, 10]
numero = 10

lista_final = soma_n_par(lista_ini, numero)
print(lista_final) 