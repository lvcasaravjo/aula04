### Exercício 10. Agregação de Dados por Categoria
# Objetivo:** Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.

vendas = [
    {"produto":"notebook","categoria" : "eletrônicos", "valor":10000},
    {"produto":"celular","categoria" : "eletrônicos", "valor":5000},
    {"produto":"geladeira","categoria" : "eletrodomestico", "valor":4000},
    {"produto":"sofa","categoria" : "movel", "valor":3000},
    {"produto":"lava-louça","categoria" : "eletrodomestico", "valor":1000}
]

total_por_categoria = {}
for venda in vendas:
    categoria = venda["categoria"]
    valor = venda["valor"]
    if categoria in total_por_categoria:
        total_por_categoria[categoria] += valor
    else:
        total_por_categoria[categoria] = valor

print(total_por_categoria)