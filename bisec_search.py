def bisec_search(meta, item, m):  # default binary search
    low, high = 0, len(meta)
    while low < high:
        mid = (low+high) // 2
        mid_val = meta[mid]
        if item > mid_val:
            low = mid+1
        elif item < mid_val:
            high = mid-1
        else:
            return [meta[mid], m, mid]
    if low == len(meta):
        low -= 1
    if meta[low] == item:
        return [meta[low], m, low]
    else:
        return [-1]
