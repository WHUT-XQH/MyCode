def shell_sort(us_list):
    """希尔排序，自写"""
    n = len(us_list)
    gap = n // 2
    while gap >= 1:
        for i in range(0, gap):
            for j in range(i, n - 1, gap):
                k = j
                while k >= i:
                    if j + gap > n - 1:
                        break
                    elif us_list[k + gap] < us_list[k]:
                        us_list[k + gap], us_list[k] = us_list[k], us_list[k + gap]
                        k -= gap
                    else:
                        break
        gap = gap // 2


def shell_sort2(us_list):
    """希尔排序，标准"""
    n = len(us_list)
    gap = n // 2
    while gap >= 1:
        for j in range(gap, n):
            i = j
            while i > 0:
                if us_list[i] < us_list[i - gap]:
                    us_list[i], us_list[i - gap] = us_list[i - gap], us_list[i]
                    i -= gap
                else:
                    break
        gap = gap // 2


if __name__ == '__main__':
    l1 = [9, 9, 8, 7, 6, 5, 6, 4, 3, 2, 1]
    shell_sort2(l1)
    print(l1)
