def merge_sort(us_list):
    """归并排序"""
    if len(us_list) <= 1:
        return us_list
    mid = len(us_list)//2
    left = merge_sort(us_list[:mid])
    right = merge_sort(us_list[mid:])
    left_pointer, right_pointer = 0, 0
    result = []
    while left_pointer < len(left) and right_pointer < len(right):
        if left[left_pointer] < right[right_pointer]:
            result.append(left[left_pointer])
            left_pointer += 1
        else: 
            result.append(right[right_pointer])
            right_pointer += 1
    result += left[left_pointer:]
    result += right[right_pointer:]
    return result


if __name__ == '__main__':
    l1 = [9, 9, 8, 7, 6, 5, 6, 4, 3, 2, 1]
    print(merge_sort(l1))

