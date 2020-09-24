import requests

kv = {'user-agent': 'Mozilla/5.0'}
kx = {'wd': 'Python'}


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30, headers=kv, params=kx)
        print(r.status_code)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text

    except:
        return "产生异常"


if __name__ == "__main__":
    url = "http://www.baidu.com"
    print(len(getHTMLText(url)))
