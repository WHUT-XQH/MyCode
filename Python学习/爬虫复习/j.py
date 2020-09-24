istr = input()
lista = istr.split(',')
s = set()
for i in lista[0]:
    if i == '"':
        continue
    else:
        s.add(i)
for j in lista[1]:
    if j == '"':
        continue
    else:
        if j in s:
            nstr = '\"' + str(j) + '\"'
            print(nstr)

