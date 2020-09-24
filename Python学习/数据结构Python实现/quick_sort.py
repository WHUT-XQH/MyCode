def quick_sort(us_list, start, end):
    """快速排序"""
    if start >= end:
        return
    mid_value = us_list[start]
    low = start
    high = end
    while low < high:
        while low < high and us_list[high] >= mid_value:
            high -= 1
        us_list[low] = us_list[high]
        while low < high and us_list[low] < mid_value:
            low += 1
        us_list[high] = us_list[low]
    us_list[low] = mid_value
    quick_sort(us_list, start, low-1)
    quick_sort(us_list, low+1, end)


if __name__ == '__main__':
    l1 = [9, 9, 8, 7, 6, 5, 6, 4, 3, 2, 1]
    quick_sort(l1, 0, len(l1)-1)
    print(l1)

