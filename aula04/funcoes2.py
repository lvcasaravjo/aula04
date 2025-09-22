#Crie uma função que receba um número como argumento e retorne True se o número for primo e False caso contrário.

def primo(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

valor = int(input('Insira um número inteiro: '))

if primo(valor) == True:
    print(f'O valor {valor} é um número primo.')
else:   
    print(f'O valor {valor} não é um número primo.')