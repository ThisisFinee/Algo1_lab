def ladder_search(a, m, n, el):  # default ladder search
    n1 = 0
    m1 = m - 1
    elem = [-1, -1, -1]
    while elem[0] != el:
        if a[n1][m1] < el and n1 < n - 1:
            n1 += 1
        elif a[n1][m1] > el and m1 > 0:
            m1 -= 1
        elif a[n1][m1] == el:
            elem = [el, n1, m1]
        else:
            break
    return elem