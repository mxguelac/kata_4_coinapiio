import requests

apikey = 'DCE5F646-586A-458F-B048-DD15FE4F5530'

url = f'https://rest.coinapi.io/v1/exchangerate/BTC/EUR?apikey={apikey}'

response = requests.get(url)

print(response.status_code)
print(response.text)