import requests
url = 'https://www.baidu.com/'
response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)'}, proxies={'http':'111.111.111.111:9997'}, timeout=30)
print(response.status_code)
print(response.text)
