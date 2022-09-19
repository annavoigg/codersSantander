# strings I 

empresa = "Google"
print(empresa)

novaEmpresa = 'Amazon'
print(novaEmpresa)

empresa = "Let's code"
print(empresa)

frase = "O professor Pietro, da Let's Code disse: \"Hoje a pizza é por minha conta\" "
print(frase)

empresa = 'Google'
print(empresa[0])
print(empresa[:3])

nomesCidades = "São Paulo, Belo Horizonte, Rio de Janeiro, Brasília"
nomesCidades = nomesCidades.split(', ')
print(nomesCidades)

cabecalho = "                MENU PRINCIPAL                "
print(cabecalho)
print(cabecalho.strip())

nomeCidade = "rIo DE jaNeiro"

print(nomeCidade)
print(nomeCidade.title())
print(nomeCidade.capitalize())
print(nomeCidade.lower())
print(nomeCidade.upper())

# exemplo 

# nomeCidade = input('Que cidade do Brasil é considerada como cidade maravilhosa? ')
# nomeCidade = nomeCidade.strip()

# while nomeCidade.lower() != 'rio de janeiro':
#     print('Tente novamente.')
#     nomeCidade = input('Que cidade do Brasil é considerada como cidade maravilhosa? ')

# print('Boa, capião!')

mensagem = 'Você viu o que o Pietro disse na sala ontem?'
fuiCitado = 'Pietro' in mensagem
print(fuiCitado)