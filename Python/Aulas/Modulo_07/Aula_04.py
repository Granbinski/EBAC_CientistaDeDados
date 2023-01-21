import json
import requests as req

response = req.get(
    'https://www2.cetip.com.br/ConsultarTaxaDi/ConsultarTaxaDICetip.aspx'
)
print(f'status code: {response.status_code}')
print(response.text)

data = json.loads(response.text)
print(data)
print(type(data))

cdi = None
for key, value in data.items():
    if key == 'taxa':
        cdi = value.replace(',', '.')
        cdi = float(cdi)
print(cdi)
print(type(cdi))
