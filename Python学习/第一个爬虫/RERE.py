import re

res = re.compile(r'[\u4e00-\u9fa5]')

match = res.finditer('l我lkj120sdfsd2s是dfsdf450')
for r in match:
    print(r)

