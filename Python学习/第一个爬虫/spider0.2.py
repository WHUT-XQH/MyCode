import requests
import os

kv = {'user-agent': 'Mozilla/5.0'}
url ="https://pic3.zhimg.com/v2-a5c142b231f5cfccc54d69410c635490_1440w.jpg?source=172ae18b"
root = "/home/xqh/桌面/tupian/"
path = root + url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url, timeout=30, headers=kv)
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
            print("文件保存成功！")
    else:print("文件已存在")
except:
    print("爬取失败")

