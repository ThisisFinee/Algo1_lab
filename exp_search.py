def bis_search(lst, item):
    low, high = 0, len(lst)
    while low < high:
        mid = (low + high) // 2
        mid_val = lst[mid]
        if item > mid_val:
            low = mid + 1
        else:
            high = mid - 1
    if low == len(lst):
        low -= 1
    if lst[low] == item:
        return [lst[low]]
    else:
        return [-1]
def exp_search(mas, item):
    if mas[0][0] == item:
        return [mas[0][0]]
    ind = 1
    while ind < len(mas[0])*len(mas)-1:
        if mas[ind//(len(mas[0]))][ind%(len(mas[0]))] > item:
            break
        else:
            ind *= 2
    if len(mas[0])*len(mas)-1 < ind:
        ind = len(mas[0])*len(mas)-1
    ind1 = ind//2
    for i in range(ind1//len(mas[0]), ind//len(mas[0])+1):
        if i == ind1//len(mas[0]) and ind1%len(mas[0]) != len(mas[0])-1:
            bs_res = bis_search(mas[i][ind1%len(mas[0]):len(mas[0])-1], item)
        elif i == ind//len(mas[0]) and ind%len(mas[0]) != 0:
            bs_res = bis_search(mas[i][0:ind%len(mas[0])], item)
        else:
            bs_res = bis_search(mas[i], item)
        if bs_res[0] != -1:
            break
    return bs_res



