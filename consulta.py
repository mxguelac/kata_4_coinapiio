import requests

apikey = 'DCE5F646-586A-458F-B048-DD15FE4F5530'
criptos = ['BTC', 'ETH', 'USDT', 'BNB', 'USDC']
fiats = ['EUR', 'USD', 'JPY']


def test_input(arrays, mensaje):
    money = input(mensaje)
    while money not in arrays:
        print('Debe ser una de las siguientes opciones', arrays)
        money = input(mensaje)
    return money

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



cripto = test_input(criptos, 'Que criptomoneda quieres saber?')
fiat = test_input(fiats, 'En que moneda la quieres?')

is_OK, data = get_rate(cripto, fiat)

if is_OK:
    print(f"1{cripto} vale {data:.2f} {fiat}")
else:
    print(f'Se ha producido el error:{data}')
