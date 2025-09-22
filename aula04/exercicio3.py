#Objetivo: Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.

#Minha resposta
idades = [12, 15, 18, 22, 10, 20, 25]
idades_filtro = []

for i in idades:
    if i > 18:
        idades_filtro.append(i)

print(idades_filtro)


#Resposta curso
idades = [22, 15, 30, 17, 18]
idades_validas = [idade for idade in idades if idade >= 18]

print(idades_validas)

