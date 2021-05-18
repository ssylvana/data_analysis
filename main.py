import requests
import json


def get_contracts_by_region(region_code):
    url = f'http://openapi.clearspending.ru/restapi/v3/contracts/search/?customerregion={region_code}'
    data = requests.get(url).json()
    return data

# Записывается в result контракты по региону region_code (в нашем случае 77 - Москва)
result = get_contracts_by_region(77)
print(result)

#Засписывает в result.json
with open('result.json', 'w') as json_file:
    json.dump(result, json_file)