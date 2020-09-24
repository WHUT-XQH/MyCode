import requests

url = "https://m.so.com/position?ip="
try:
    r = requests.get(url + '192.168.3.103')
    r.raise_for_status()
    print(r.status_code)
    r.encoding = r.apparent_encoding
    print(r.text[-500:])
except:
    print("爬取失败")

