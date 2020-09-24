def binary_search(sorted_list, num, start, end):
    """二分查找,自写"""
    if end == start and num == sorted_list[end]:
        return end
    elif end == start and num != sorted_list[end]:
        return '没找到'
    else:
        mid = (end + start)//2
        if num == sorted_list[mid]:
            return mid
        elif num < sorted_list[mid]:
            return binary_search(sorted_list, num, start, mid-1)
        elif num > sorted_list[mid]:
            return binary_search(sorted_list, num, mid+1, end)


def binary_search2(sorted_list, num):
    """二分查找,标准，使用递归"""
    n = len(sorted_list)
    if n > 0:
        mid = n // 2
        if num == sorted_list[mid]:
            return True
        elif num < sorted_list[mid]:
            return binary_search2(sorted_list[:mid], num)
        else:
            return binary_search2(sorted_list[mid+1:], num)
    return False


def binary_search3(sorted_list, num):
    """二分查找,标准，不使用递归"""
    n = len(sorted_list)
    first = 0
    last = n-1
    while first <= last:
        mid = (first + last) // 2
        if num == sorted_list[mid]:
            return True
        elif num < sorted_list[mid]:
            last = mid - 1
        else:
            first = mid + 1
    return False


if __name__ == '__main__':
    l1 = [1, 2, 4, 5, 6, 7, 9]
    index = binary_search3(l1, 0)
    print(index)
