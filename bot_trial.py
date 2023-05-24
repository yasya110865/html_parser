import requests


TOKEN = '6044805267:AAHsTIfVbVfmIRu9ifZtj2IhiagTTr5Ree0'

MAIN_URL = f'https://api.telegram.org/bot{TOKEN}'

url = f'{MAIN_URL}/getMe'
result = requests.get(url)
print(result.json())

# /172.67.167.139