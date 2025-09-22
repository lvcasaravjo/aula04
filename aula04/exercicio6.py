#Objetivo: Dada uma lista de valores, dividir em duas listas: uma para valores pares e outra para ímpares.

valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pares = [valor for valor in valores if valor % 2 == 0]
impares = [valor for valor in valores if valor % 2 != 0]

print(f'lista de números pares: {pares}')
print(f'lista de números ímpares: {impares}')