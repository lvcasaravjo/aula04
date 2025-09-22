#Desenvolva uma função que receba uma string como argumento e retorne essa string revertida.

def inverte_texto(t: str) -> str:
    return t[::-1]

texto = input('Digite um texto: ')
print(f'O texto digitado invertido é {inverte_texto(texto)}.')