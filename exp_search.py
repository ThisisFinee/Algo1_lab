def bis_search(lst, start, stop, item):
    mid = (start + stop) // 2
    if start > stop:
        return [-1, start]
    if item == lst[mid-1]:
        return [1, mid]
    elif item < lst[mid-1]:
        return bis_search(lst, start, mid - 1, item)
    else:
        return bis_search(lst, mid + 1, stop, item)


def exp_s(arr, start, end, num, exp=1):
    s_end = max(end-2**exp, start)
    if arr[s_end] == num:
        return [1, s_end]
    elif arr[s_end] < num or s_end == start:
        return bis_search(arr, s_end, end, num)
    else:
        return exp_s(arr, start, s_end, num, exp+1)


def exp_search(matrix, col_len, string_len, num):
    rez = exp_s(matrix[0], 0, string_len, num)
    if rez[0] == 1:
        return [0, rez[1]]
    for i in range(1, col_len):
        rez = exp_s(matrix[i], 0, rez[1]-1, num)
        if rez[0] == 1 or (rez[1] == 0 and matrix[i][0] > num):
            return [i, rez[1]]
    if rez[0] == -1:
        return [-1]

