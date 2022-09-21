import requests as r
import datetime as dt
import csv
from PIL import Image
from IPython.display import display
from urllib.parse import quote


url = 'https://api.covid19api.com/dayone/country/brazil'

resp = r.get(url)
# print(resp.status_code)

rawData = resp.json()
# print(rawData[0])

finalData = []
for obs in rawData:
    finalData.append([obs['Confirmed'], obs['Deaths'], obs['Recovered'], obs['Active'], obs['Date']])

finalData.insert(0, ['Confirmados', 'Óbitos', 'Recuperados', 'Ativos', 'Data'])
# print(finalData) 

CONFIRMADOS = 0
OBITOS = 1
RECUPERADOS = 2
ATIVOS = 3
DATA = 4

for i in range(1, len(finalData)):
    finalData[i][DATA] = finalData[i][DATA][:10]


with open('projeto/brasilCovid.csv', 'w', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(finalData)

for i in range(1, len(finalData)):
    finalData[i][DATA] = dt.datetime.strptime(finalData[i][DATA], '%Y-%m-%d')

# print(finalData)

def getDataSets(y, labels):
    if type(y[0]) == list:
        datasets = []
        for i in range(len(y)):
            datasets.append({
                'label': labels[i],
                'data': y[i]
            })
        return datasets
    else:
        return [
            {
                    'label': labels[0],
                    'data': y
            }
        ]

def setTitle(title=''):
    if title != '':
        display = 'true'
    else:
        display = 'false'
    return{
        'title': title,
        'display': display
    }

def createChart(x, y, labels, kind='bar', title=''):
    datasets = getDataSets(y, labels)
    options = setTitle(title)

    chart = {
        'type': kind,
        'data': {
            'labels': x,
            'datasets': datasets
        },
        'options': options
    }
    return chart

# função que faz  requisição na api utilizando o dicionário 
def getApiChart(chart):
    url_base = 'https://quickchart.io/chart'
    resp = r.get(f'{url_base}?c={str(chart)}')
    return resp.content

def saveImage(path, content):
    with open(path, 'wb') as image:
        image.write(content)



def displayImage(path):
    imgPil = Image.open(path)
    display(imgPil)

yData1 = []
for obs in finalData[1::10]:
    yData1.append(obs[CONFIRMADOS])

yData2 = []
for obs in finalData[1::10]:
    yData2.append(obs[RECUPERADOS])

labels = ['Confirmados', 'Recuperados']

x = []
for obs in finalData[1::10]:
    x.append(obs[DATA].strftime('%d/%m/%Y'))

chart = createChart(x, [yData1, yData2], labels, title='Gráfico confirmados vs recuperados')
chartContent = getApiChart(chart)
saveImage('projeto/meu-primeiro-grafico.png', chartContent)
displayImage('projeto/meu-primeiro-grafico.png')



def getApiQrcode(link):
    text = quote(link) #parse do link para url
    url_base = 'http://quickchart.io/qr'
    resp = r.get(f'{url_base}?text={text}')
    return resp.content

url_base = 'https://quickchart.io/chart'
link = f'{url_base}?c={str(chart)}'
saveImage('qr-code.png', getApiQrcode(link))
displayImage('projeto/qr-code.png')