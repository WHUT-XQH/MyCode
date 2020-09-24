arry = [3,4,5]
def abs1(a):
    if a >= 0:
        return a
    else:
        return -a
l = len(arry)
if l >= 3:
    maxl = 0
    for i in range(0, l):
        for j in range(0, l):
            if i == j:
                continue
            else:
                for k in range(0, l):
                    if k == i or k == j:
                        continue
                    else:
                        if (arry[i] + arry[j] > arry[k]) and (abs1(arry[i] - arry[j]) < arry[k]):

                            if arry[i] + arry[j] + arry[k] > maxl:
                                maxl = arry[i] + arry[j] + arry[k]
    print(maxl)
else:
    print(0)

