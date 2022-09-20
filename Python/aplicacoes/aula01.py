# manipulação de arquivos 

from turtle import width


arquivo = open('aplicacoes/alunos.csv', 'r', encoding='utf-8')

# armazenando o texto na varíavel pra exibi-lo 

texto = arquivo.read()
print(texto)
arquivo.close()

# armazenando o texto na variável pra ler linha a linha 

arquivo = open('aplicacoes/alunos.csv', 'r', encoding='utf-8')
linha = arquivo.readline()

# mostrando linha a linha com while até quebrar o loop com end 

while linha != '':
    print(linha, end=' ')
    linha = arquivo.readline()
arquivo.close()

arquivo = open('aplicacoes/alunos.csv', 'r', encoding='utf-8')

for linha in arquivo:
    print(linha, end=' ')
arquivo.close()

# método 'r' serve para ler o arquivo 

with open('aplicacoes/alunos.csv', 'r', encoding='utf-8') as arquivo:
    text = arquivo.read()
    print(text)

# método 'w' serve para escrever no arquvi 

with open('aplicacoes/teste.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write('Essa é uma linha que eu escrevi usando Python\n')
    arquivo.write('Essa é a segunda linha que eu escrevi usando Python\n')

with open('aplicacoes/teste.txt', 'r', encoding='utf-8') as arquivo:
    print(arquivo.read(), end=' ')

# método 'a' serve para adicionar algo ao arquivo sem sobrescrever o que já está nele 

with open('aplicacoes/teste.txt', 'a', encoding='utf-8') as arquivo:
    arquivo.write('Essa é a terceira linha que eu escrevi com Python\n')
