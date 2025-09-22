#Escreva uma função que receba um dicionário e retorne uma lista de chaves ordenadas

dicionario = {"a": 1, "b": 2, "c": 3}

#alternativa com método sort
# def ord_chaves(dict: dict) -> list:
#     chaves = list(dict.keys())
#     chaves.sort()
#     return chaves

# print(ord_chaves(dicionario))

#alternativa com método sorted 

def ord_chaves(dict: dict) -> list:
    return sorted(dict.keys())

print(ord_chaves(dicionario))