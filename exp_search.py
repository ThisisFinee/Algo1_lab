def bis_search(lst, item):
    low, high = 0, len(lst)
    while low < high:
        mid = (low + high) // 2
        mid_val = lst[mid]
        if item > mid_val:
            low = low + 1
        else:
            high = mid - 1
    if lst[low] == item:
        return [lst[low]]
    else:
        return [-1]
def exp_search(meta, item):
    meta1 = []
    if meta[0] == item:
        return [1]
    ind = 1
    while meta[ind] < item:
        ind*=2
        if ind >= len(meta):
            ind = len(meta)-1
            if meta[ind] < item:
                return [-1]
            else:
                break
    return ind


