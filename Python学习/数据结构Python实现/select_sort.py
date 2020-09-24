def select_sort(us_list):
    n = len(us_list)
    for j in range(n-1):
        min_idx = j
        for i in range(j+1, n):
            if us_list[min_idx] > us_list[i]:
                min_idx = i
        us_list[j], us_list[min_idx] = us_list[min_idx], us_list[j]


if __name__ == '__main__':
    l = [18, 19, 40, 28, 60, 53]
    select_sort(l)
    print(l)

