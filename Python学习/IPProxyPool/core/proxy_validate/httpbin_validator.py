# 校验模块
import time
import requests
from utils.http import get_request_headers
from settings import TEST_TIMEOUT
import json
from utils.log import logger
from domain import Proxy


def check_proxy(proxy):
    # 检查指定的代理ip
    proxies = {
        'http': 'http://{}:{}'.format(proxy.ip, proxy.port),
        'https': 'https://{}:{}'.format(proxy.ip, proxy.port)
    }

    # 测试代理ip
    http, http_nick_type, http_speed = __check_http_proxies(proxies)
    https, https_nick_type, https_speed = __check_http_proxies(proxies, False)

    if http and https:
        proxy.protocol = 2
        proxy.nick_type = http_nick_type
        proxy.speed = http_speed
    elif http:
        proxy.protocol = 0
        proxy.nick_type = http_nick_type
        proxy.speed = http_speed
    elif https:
        proxy.protocol = 1
        proxy.nick_type = https_nick_type
        proxy.speed = https_speed
    else:
        proxy.protocol = -1
        proxy.nick_type = -1
        proxy.speed = -1
    return proxy


def __check_http_proxies(proxies, is_http=True):
    nick_type = -1
    speed = -1
    if is_http:
        test_url = 'http://httpbin.org/get'
    else:
        test_url = 'https://httpbin.org/get'
    try:
        start = time.time()  # 获取开始时间
        # 发送请求，获取响应数据
        response = requests.get(test_url, headers=get_request_headers(), proxies=proxies, timeout=TEST_TIMEOUT)
        print(response.status_code)

        if response.ok:
            # 计算响应速度
            speed = round(time.time() - start, 2)
            # 计算匿名程度
            dic = json.loads(response.text)
            origin = dic['origin']
            proxy_connection = dic['headers'].get('Proxy-Connection', None)
            if ',' in origin:
                nick_type = 2  # 透明代理
            elif proxy_connection:
                nick_type = 1  # 匿名代理
            else:
                nick_type = 0  # 高匿代理

            return True, nick_type, speed
        return False, nick_type, speed
    except Exception as ex:
        return False, nick_type, speed


if __name__ == '__main__':

    proxy = Proxy('218.64.148.180', port='9000')
    print(check_proxy(proxy))