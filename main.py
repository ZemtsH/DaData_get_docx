import json
import requests as requests

from docxtpl import DocxTemplate

API_KEY = 'b9381a653f85a0d5cf6da7117b70d2c7ee660985'
API_SECRET = 'ac84ea6c8dc7e454ff2beeed6aefb30ac42b2e84'

BASE_URL = 'https://suggestions.dadata.ru/suggestions/api/4_1/rs/suggest/'



def findName(resource, query):
    url = BASE_URL + resource
    headers = {
        'Authorization': 'Token ' + API_KEY,
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    data = {
        'query': query
    }
    res = requests.post(url, data=json.dumps(data), headers=headers)
    return res.json()

def testWord(executor, client):
    doc = DocxTemplate("dogovor.docx")
    context = {
        'executorName': executor['suggestions'][0]['value'],
        'executorDirector': executor['suggestions'][0]['data']['management']['post'] +
                            ": " + executor['suggestions'][0]['data']['management']['name'],
        'executorINN': executor['suggestions'][0]['data']['inn'],
        'executorKPP': executor['suggestions'][0]['data']['kpp'],
        'executorOGRN': executor['suggestions'][0]['data']['ogrn'],
        'executorAddress': executor['suggestions'][0]['data']['address']['value'],

        'clientName': client['suggestions'][0]['value'],
        'clientDirector': client['suggestions'][0]['data']['management']['post'] +
                          ": " + client['suggestions'][0]['data']['management']['name'],
        'clientINN': client['suggestions'][0]['data']['inn'],
        'clientKPP': client['suggestions'][0]['data']['kpp'],
        'clientOGRN': client['suggestions'][0]['data']['ogrn'],
        'clientAddress': client['suggestions'][0]['data']['address']['value'],
        }
    doc.render(context)
    doc.save("dogovor-data.docx")


if __name__ == '__main__':
    clientName = str(input("Введите название фирмы А: "))
    executorName = str(input("Введите название фирмы Б: "))
    executor = findName('party', executorName)
    client = findName('party', clientName)
    testWord(executor, client)


