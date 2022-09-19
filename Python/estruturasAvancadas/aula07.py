# funções II 

def calculaMedia(valor1, valor2, valor3):
    soma = valor1 + valor2 + valor3
    media = soma / 3
    return media

def calculaMedia(*args):
    soma = sum(args)
    media = soma / len(args)
    return media

print(calculaMedia(10,8,9))

def printInfo(**kwargs):
    print(kwargs, type(kwargs))

printInfo(nome='Giovanna', sobrenome='Gomes')