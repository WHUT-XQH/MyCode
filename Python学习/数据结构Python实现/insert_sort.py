def insert_sort(us_list):
    n = len(us_list)
    for i in range(1, n):
        j = i
        while j > 0:
            if us_list[j] < us_list[j-1]:
                us_list[j], us_list[j-1] = us_list[j-1], us_list[j]
                j -= 1
            else:
                break


if __name__ == '__main__':
    l = [18, 19, 40, 28, 60, 53]
    insert_sort(l)
    print(l)




