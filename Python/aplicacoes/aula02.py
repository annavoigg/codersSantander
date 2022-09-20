# arquivos csv 

# importando a biblioteca
from asyncore import write
import csv

with open('aplicacoes/alunos.csv', 'r', encoding='utf-8') as arquivo:
    leitor = csv.reader(arquivo)
    next(leitor)
    header = next(leitor)
    for linha in leitor:
        if linha[2] > ' ':
            print(linha)

# acessando o arquivo csv apenas com o python ao o transformar em lista, sem a biblioteca, e obtendo basicamente o mesmo resultado

with open('aplicacoes/alunos.csv', 'r', encoding='utf-8') as arquivoCsv:
    linhas = arquivoCsv.read()
    linhas = linhas.split('\n')
    for linha in linhas:
        linha = linha.split(',')
        print(linha, type(linha))

with open('aplicacoes/user.csv', 'w', encoding='utf', newline='') as arquivoUsers:
    escritor = csv.writer(arquivoUsers)
    escritor.writerow(['nome', 'sobrenome', 'email', 'gênero'])
    escritor.writerow(['Giovanna', 'Gomes', 'gomesgiovanna006@gmail.com', 'Feminino'])

# exemplo 

# criação do cabeçalho: 
header = ['nome', 'sobrenome']
# criação de lista vazia que irá guardar todos os dados: 
dados = []
#input para coletar dados
opt = input('O que você deseja fazer?\n1 - Cadastrar\n0 - Sair\n')
#caso ele não digite sair:
while opt != '0':
    nome = input('Qual o seu nome? ')
    sobrenome = input('Qual o seu sobrenome? ')
# adicionando a lista à lista existinte:
    dados.append([nome, sobrenome])
    opt = input('O que deseja fazer?\n1 - Cadastrar\n0 - Sair\n')

print(dados)

with open('user.csv', 'w', newline='', encoding='utf-8') as arquivoCsv:
# criando o escritor e selecionando o arquivo que vamos escrever:
    writer = csv.writer(arquivoCsv)
# escrevendo o header
    writer.writerow(header)
# escrevendo os dados
    writer.writerow(dados)

# abrindo o arquivo como leitor apenas para ter certeza de que tudo deu certo: 
with open('user.csv', 'r', encoding='utf-8') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')
    for linha in csvReader:
        print(linha)