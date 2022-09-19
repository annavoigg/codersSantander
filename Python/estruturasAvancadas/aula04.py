# dicionários 

dadosCidade = {
    'nome': 'São Paulo',
    'estado': 'São Paulo',
    'areaKm2': 1521,
    'populacaoMilhoes': 12.18
}

print(type(dadosCidade))
print(dadosCidade)

dadosCidade['pais'] = 'Brasil'
print(dadosCidade)

print(dadosCidade['nome'])

dadosCidade['areaKm2'] = 1500
print(dadosCidade)

dadosCidade2 = dadosCidade
dadosCidade2 ['nome'] = 'Santos'
print(dadosCidade2)
print(dadosCidade)

dadosCidade ['nome'] = 'São Paulo'

dadosCidade3 = dadosCidade.copy()
dadosCidade3 ['nome'] = 'Rio de Janeiro'
print(dadosCidade3)
print(dadosCidade)

# atualizando dict original com novos dados 

novosDados = {
    'populacaoMilhoes': 15,
    'fundacao': '25/01/1554'
}

dadosCidade.update(novosDados)
print(dadosCidade)

print(dadosCidade.get('Prefeito'))

# métodos que transformam dicionários em lista 

print(dadosCidade.keys()) # retorna uma lista de chaves de um dicionário
print(dadosCidade.values()) # retorna uma lista de valores de um dicionário
print(dadosCidade.items()) # retorna uma lista de tuplas (chave, valor) de um dicionário