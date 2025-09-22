precos = {"maçã": 10, "banana": 30, "cereja": 65}

preco_att = {produto: preco for produto, preco in precos.items() if preco < 50}
print(preco_att)