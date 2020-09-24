import requests

def get_proxy():
    return requests.get('http://localhost:5010/get/')

def delete_proxy(proxy):
    requests.get('http://localhost:5010/delete/?proxy={}'.format(proxy))

print(get_proxy())
