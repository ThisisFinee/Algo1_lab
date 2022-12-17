def bisec_search(meta, item):  # default binary search
    low, high = 0, len(meta)
    while low < high:
        mid = (low+high) // 2
        mid_val = meta[mid]
        if item > mid_val:
            low = mid+1
        elif item < mid_val:
            high = mid-1
        else:
            return [meta[low]]
    if low == len(meta):
        low -= 1
    if meta[low] == item:
        return [meta[low]]
    else:
        return [-1]
