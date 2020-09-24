import time


def bubble_sort(unsorted_list):
    """自己写的，效率不高"""
    if list:
        while True:
            cur = unsorted_list[0]
            n = 0
            for index, i in enumerate(unsorted_list):
                if cur > i:
                    arg = unsorted_list[index]
                    unsorted_list[index] = cur
                    unsorted_list[index - 1] = arg
                    n += 1
                elif cur <= i:
                    cur = unsorted_list[index]
            if n == 0:
                break
        return unsorted_list


def bubble_sort2(unsorted_list):
    """标准代码"""
    n = len(unsorted_list)
    for j in range(0, n - 1):
        count = 0
        for i in range(0, n - 1 - j):
            if unsorted_list[i] > unsorted_list[i + 1]:
                unsorted_list[i], unsorted_list[i + 1] = unsorted_list[i + 1], unsorted_list[i]
                count += 1
        if 0 == count:
            break
    return unsorted_list


if __name__ == '__main__':
    list1 = [5, 4, 3, 3, 2, 2, 1, 5, 4, 3, 3, 2, 2, 1]
    start_time = time.time()
    print(bubble_sort(list1))
    end_time = time.time()
    print(end_time - start_time)

    start_time2 = time.time()
    print(bubble_sort2(list1))
    end_time2 = time.time()
    print(end_time2 - start_time2)

