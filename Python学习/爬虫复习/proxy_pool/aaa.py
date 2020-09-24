import re
import sys

str1 = sys.stdin.readline()
list1 = str1.split(" ")
str2 = list1[0]
print(str2)
str3 = list1[1]
print(len(str3))
mg = ''
for wd in str3.strip():
    mg = mg + str(wd) + '?'+'.*'
print(mg)
pattrn = re.compile(mg)
mglist = pattrn.findall(str2)
print(mglist)
for i in mglist:
    if len(i) >= int((len(str3)-1)*0.8):
        str2 = re.sub(i, "*"*(len(str3)-1), str2)
print(str2)
