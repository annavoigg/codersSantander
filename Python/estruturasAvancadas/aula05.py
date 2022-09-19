# estruturas de repetição - for 

# lista 

from turtle import pos


nomesCidades = ('São Paulo', 'Londres', 'Tóquio', 'Paris')

for nome in nomesCidades:
    print(nome)

# tupla 

nomesCidades = 'São Paulo', 'Londres', 'Tóquio', 'Paris'

for nome in nomesCidades:
    print(nome)

# dicionario 

cidade = {
    'nome': 'São Paulo',
    'estado': 'São Paulo',
    'populacaoMilhoes': 12.2
}

for chave in cidade:
    print(f'{chave}: {cidade[chave]}')

nomesCidades = ['São Paulo', 'Londres', 'Tóquio', 'Paris']

for nome in nomesCidades:
    nome = 'Rio de Janeiro'
print(nomesCidades)

for posicao in range(len(nomesCidades)):
    nomesCidades[posicao] = 'Rio de Janeiro'
print(nomesCidades)

print(list(range(10))) #cria uma lista de 0 até esse valor -1
print(list(range(2,10))) #especificando um valor inicial para a funçãol, ou seja, caso não queira que ela comece em 0 podemos dizer o valor
print(list(range(2,10,2))) #especificando o valor inicial, o valor final e um incremento a cada interação