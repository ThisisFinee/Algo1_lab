def ladder_search(a, m, n, el):  # default ladder search
    no_res = False
    n1 = 0
    m1 = m - 1
    elem = [-1, -1, -1]
    while elem != el or no_res != True:
        if a[n1][m1] < el and n1 < n - 1:
            n1 += 1
        elif a[n1][m1] > el and m1 > 0:
            m1 -= 1
        elif a[n1][m1] == el:
            elem = [el, n1, m1]
            break
        else:
            no_res = True
            break
    return elem