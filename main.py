import requests
from datetime import datetime

base = "https://fapi.binance.com"
path = '/fapi/v1/premiumIndex'
url = base + path
param = {'symbol': 'XRPUSDT'}
maxprice = 0
thishour = 0

while True:
    r = requests.get(url, params=param)

    if r.status_code == 200:
        data = r.json()
    else:
        print('error')

    unixtime = data['time'] / 1000
    nowtime = int(datetime.utcfromtimestamp(unixtime).strftime('%H'))

    if nowtime == 00:
        thishour = nowtime
        maxprice = 0
    elif nowtime > thishour:
        thishour = nowtime
        maxprice = 0

    if maxprice < float(data['markPrice']):
        maxprice = float(data['markPrice'])

    if float(data['markPrice']) <= maxprice - (maxprice * 0.01):
        maxprice = float(data['markPrice'])
        print(f'XRP/USDT упала в цене на 1% и более в течении {thishour}-го часа')
