print('dit is een demo')
import requests

assert requests.get('http://localhost:5678').text == 'hallo\n'
