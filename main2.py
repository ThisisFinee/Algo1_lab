if __name__ == '__main__':
    from exp_search import exp_search
    from ladder_search import ladder_search
    from bisec_search import bisec_search
    import time
    for j in range(1, 14):
        strin_len = 2**13
        col_len = 2**j
        target = 16*strin_len+1
        mat = [[0] * strin_len for i in range(col_len)]
        for i in range(col_len):
            for k in range(strin_len):
                if i == 0 and k == 0:
                    mat[i][k] = 0
                else:
                    mat[i][k] = int((strin_len/col_len*i*k)*2)
        print(f"Размер матрицы: Количество строк: {col_len}, Количество столбцов: {strin_len}")
        start_time1 = time.process_time()
        for k in range(1000):
            lad_res = ladder_search(mat, strin_len, col_len, target)
        end_time1 = time.process_time()
        lad_res.append((end_time1 - start_time1))
        if lad_res[0] == -1:
            print(f"{j}.В результате поиска лесенкой элемент не был найден, время: {lad_res[3]}")
        else:
            print(
                f"{j}.Поиск лесенкой.Элемент:{lad_res[0]}, строка:{lad_res[1] + 1}, столбец:{lad_res[2]}, время:{lad_res[3]}")

        start_time2 = time.process_time()
        for k in range(1000):
            for m in range(len(mat)):
                bis_res = bisec_search(mat[m], target, m)
                if bis_res[0] != -1:
                    break
        end_time2 = time.process_time()
        bis_res.append(end_time2 - start_time2)
        if bis_res[0] == -1:
            print(f"{j}.В результате двоичного поиска элемент не был найден, время: {bis_res[1]}")
        else:
            print(
                f"{j}.Двоичный поиск.Элемент:{bis_res[0]}, cтрока:{bis_res[1] + 1}, cтолбец:{bis_res[2]}, время:{bis_res[3]}")

        start_time3 = time.process_time()
        for i in range(1000):
            exp_res = exp_search(mat, col_len, strin_len, target)
        end_time3 = time.process_time()
        if exp_res[0] != -1:
            exp_res.insert(0, mat[exp_res[0]][exp_res[1] - 1])
        exp_res.append(end_time3 - start_time3)
        if exp_res[0] == -1:
            print(f"{j}.В результате экспоненциального поиска элемент не был найден, время: {exp_res[1]}")
        else:
            print(
                f"{j}.Экспоненциальный поиск.Элемент:{exp_res[0]}, строка:{exp_res[1] + 1}, столбец:{exp_res[2] - 1}, время:{exp_res[3]}")




