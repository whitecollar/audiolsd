import requests

token = input('Enter bot token: ')
chat_id = input('Enter cat id: ')
number = input('Enter number: ')

url = f'https://api.telegram.org/bot{token}/sendContact'
p = {'first_name': 'Unknown name', 'chat_id': chat_id, 'phone_number': number}

r = requests.get(url, params=p)
r = r.json()
try:
    print(r['result']['contact']['user_id'])
except:
    print('Not Found')
    print(r)