import requests

criptos = ['BTC', 'ETH', 'USDT', 'BNB', 'USDC']
fiats = ['EUR', 'USD', 'JPY']
apikey = 'DCE5F646-586A-458F-B048-DD15FE4F5530'

def get_rate(cripto, fiat):
    url = f'https://rest.coinapi.io/v1/exchangerate/{cripto}/{fiat}?apikey={apikey}'
    try:
        response = requests.get(url)
        data = response.json()
        if response.status_code == 200: 
            return True, data['rate']   
            #print(f"1{cripto} vale {data['rate']:.2f} {fiat}")
        else:
            return False, data['error']
            #print(response.status_code, "-", data['error'])
    except requests.exceptions.RequestException:
        return False, str(e)
        #print('Se ha producido un error en la peticion:\n', url)

