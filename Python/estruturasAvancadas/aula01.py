# listas 

nomesPaises = ['Brasil', 'Argentina', 'China', 'Canadá', 'Japão']

print(nomesPaises)

print('Tamanho da lista: ', len(nomesPaises))

print('Acessando um item dentro da variável: ', nomesPaises[4])

print('Acessando o último item da lista usando um índice negativo, que funciona de trás para frente: ', nomesPaises[-1])

nomesPaises[4] = 'Colômbia'
print('E assim foi feita uma alteração, sobrescrevendo o último item da variável: ', nomesPaises[4])

print('Tamanho da lista: ', len(nomesPaises))

print('Selecionando os itens da lista entre os dois parâmetros passados', nomesPaises[0:2])

print('Ocultando os primeiros itens da lista: ', nomesPaises[2:])

print('Ocultando ambos oa valores: ', nomesPaises[:])

print('Pulando itens de dois em dois: ', nomesPaises[::2])

print('Invertendo os itens de uma lista: ', nomesPaises[::-1])

print('Verificando se existe determinado elemento dentro da lista: ', 'Brasil' in nomesPaises)

print('Verificando se não existe determinado elemento dentro da lista: ', 'Canadá' not in nomesPaises)

listaCapitais = []

listaCapitais.append('Brasília')
listaCapitais.append('Buenos Aires')
listaCapitais.append('Pequim')
listaCapitais.append('Bogotá')

print(listaCapitais)

listaCapitais.insert(2, 'Paris')
print(listaCapitais)

print(len(listaCapitais))

listaCapitais.remove('Buenos Aires')
print(listaCapitais)

itemRemovido = listaCapitais.pop(2)
print(listaCapitais, itemRemovido)

# tuplas 

nomesPaises = ('Brasil', 'Argentina', 'China', 'Canadá', 'Japão')
print(nomesPaises, type(nomesPaises))

nomeTeste = 'Bogotá', 'Buenos Aires', 'EUA'
print(nomeTeste, type(nomeTeste))

nomeEstado = 'São Paulo',
print(nomeEstado, type(nomeEstado))

print(len(nomesPaises))

br, arg, ch, ca, jp = nomesPaises
print(br, ch, jp)

print(*nomesPaises)