import requests

def get_btc_price():
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    data = response.json()
    x = data["bpi"]["USD"]["rate"]
    return x