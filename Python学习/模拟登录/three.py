import requests
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

try:
    url = 'http://sso.jwc.whut.edu.cn/Certification/login.do'
    r = requests.Session()
    res =r.post(url, headers=header, data={'code': '2494376255',
                                                 'rnd':'1317',
                                                 'userName1': '2940c5e09b94d7e9df320047baedfc76',
                                                 'password1': 'bfa3ec7159f227ec5b3fd740f60f876a0233f6a8',
                                                 'webfinger': '736b9476744010bf0171061f11f74593',
                                                 'type': 'xs',
                                                 'userName': '0121709361026',
                                                 'password': 'xuqihang123456'})
    r.raise_for_status()
    print(r.text)
except:
    print("登录失败")
