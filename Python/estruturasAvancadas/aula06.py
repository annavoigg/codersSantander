# funções 

from email.policy import default


def hello ():
    print('Hello, world!')

hello()

# função com parametros para receber valores  

def calculaMedia(valor1, valor2, valor3):
    soma = valor1 + valor2 + valor3
    media = soma / 3
    return media

# armazenando o resultado em outra variável e passando os parâmtros da função 

resultado = calculaMedia(9,10,8)
print(resultado)

# deixando os valores já definidos para apenas exibir 

resultado2 = calculaMedia(valor1=9, valor2=10, valor3=9)
print(resultado2)

print('Olá,', end=' ')
print('Giovanna')

# definindo valores default caso não sejam inseridos valores na funções

def calculaMedia(valor1=0, valor2=0, valor3=0):
    soma = valor1 + valor2 + valor3
    media = soma / 3
    return media

resultado = calculaMedia()
print(resultado)