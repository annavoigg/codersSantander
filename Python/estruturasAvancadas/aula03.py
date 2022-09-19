# strings pt. II 

cumprimento = 'Olá, '
nome = 'Giovanna'
print(cumprimento + nome)

print(nome * 5 )

nome = 'Felipe'
idade = 35
nFilhos = 2
print(nome + ' tem ' + str(idade) + ' anos e ' + str(nFilhos) + ' filhos.')

print('{} tem {} anos e {} filhos'.format(nome, idade, nFilhos))

precoGasolina = 3.476
print('O preço da gasolina hoje subiu e está em R$ {:.2f}'.format(precoGasolina))

print(f'{nome} tem {idade} anos e {nFilhos} filhos')
