import requests

url = 'https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?resource_id=6899&query=失信人&pn=30&rn=10&ie=utf-8&oe=utf-8'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
           'Referer' : 'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=%E5%A4%B1%E4%BF%A1%E4%BA%BA%E5%90%8D%E5%8D%95&fenlei=256&oq=%25E7%2599%25BE%25E5%25BA%25A6%25E5%25A4%25B1%25E4%25BF%25A1%25E4%25BA%25BA%25E6%259F%25A5%25E8%25AF%25A2&rsv_pq=fe8a938b000604b2&rsv_t=79abaVRmBU98o1Ln3uUsGSwWwOaWpu9jGop8ogZJx7DZuoFasCyrwTrveTU&rqlang=cn&rsv_enter=0&rsv_dl=tb&rsv_btype=t&inputT=3338&rsv_sug3=60&rsv_sug1=34&rsv_sug7=100&rsv_sug2=0&rsv_sug4=3338'}
r = requests.get(url, headers=headers)
print(r.content.decode())