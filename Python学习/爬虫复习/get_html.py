import requests

url = 'https://www.baidu.com'
url2 = 'http://localhost:8050/render.html?url=https://www.baidu.com&timeout=30&wait=0.5'
headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'}
# response = requests.get(url,headers=headers)
# with open('1.txt', 'wb') as f:
#     f.write(response.content)
res = requests.get(url2,headers=headers)
with open('2.txt', 'wb') as x:
    x.write(res.content)