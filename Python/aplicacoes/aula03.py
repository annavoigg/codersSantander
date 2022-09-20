# APIs 

import requests

url = 'https://api.exchangerate-api.com/v6/latest'

requisicao = requests.get(url)

print(requisicao.status_code)

# recuperando dados da requisição e transformando em um dicionário
dados = requisicao.json()
print(dados)

# recuperando e transformando o valor recebido no input em tipo float 
valorReais = float(input('Informe o valor em R$ a ser convertido: \n'))
# recuperando o valor da taxa de cotação com a dados[na posicao][dentro de rates a chave BRL] 
cotacao = dados['rates']['BRL']
print(f'R${valorReais:} em dolar valem US${(valorReais / cotacao):.2f}')
