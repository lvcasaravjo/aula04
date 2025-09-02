### Exercício 9. Extração de Subconjuntos de Dados
# Objetivo:** Dada uma lista de números, extrair apenas aqueles que são pares.

lista = [2, 3, 4, 5, 8, 10, 13, 1, 20, 80, 52]

pares = [x for x in lista if x % 2 == 0]

print(pares)
