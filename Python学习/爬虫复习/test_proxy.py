import requests
import telnetlib

ip = '60.13.42.226 '
port = 9999
try:
    telnetlib.Telnet(ip, port, timeout=5)
    print('可用')
except Exception as e:
    print(e, '不可用')
