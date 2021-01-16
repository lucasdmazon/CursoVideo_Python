import requests

try:
    response = requests.get('http://pudim.com.br/')
except:
    print('\033[31mO site Pudim não está acessivel no momento.')
else:
    print('\033[32mConsegui acessar o site Pudim com sucesso!')
