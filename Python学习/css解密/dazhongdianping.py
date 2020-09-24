import requests

def gethtml(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        print(r.status_code)
        return r.text
    except:
        print("shibai")


url = 'http://www.dianping.com/yibin/ch10'
gethtml(url)