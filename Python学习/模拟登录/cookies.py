import requests

header = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Length': '264',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': 'JSESSIONID=04FB866D5FFD705135027CDD53958882',
    'Host': 'sso.jwc.whut.edu.cn',
    'Origin': 'http://sso.jwc.whut.edu.cn',
    'Referer': 'http://sso.jwc.whut.edu.cn/Certification/toLogin.do',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'}


def login():
    try:
        url = "http://sso.jwc.whut.edu.cn/Certification/toIndex.do"
        session = requests.Session()
        r = session.get(url, headers=header)
        r.raise_for_status()
        print(r.status_code)
        return r.text
    except:
        print('登录失败')


html = login()
print(html)