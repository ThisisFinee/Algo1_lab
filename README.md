# Отчёт
---
## Замеры [здесь](https://drive.google.com/drive/folders/1h-tbP_xnionJwpWfB0F-ihF1Rc0Gd5Jn?usp=sharing)
---
# Код формирования таблиц
---
## Первый вариант формирования таблицы
* ***A[i][j] == (N/M * i + j) * 2***

```python
  mat = [[0] * strin_len for i in range(col_len)]
  for i in range(col_len):
      for k in range(strin_len):
          if i == 0 and k == 0:
              mat[i][k] = 0
          else:
              mat[i][k] = int((strin_len/col_len*i+k)*2)
```
### Для запуска программы с первым формированием таблицы нужно запустить файл [main.py](https://github.com/ThisisFinee/Algo1_lab/blob/ee4f9a06513449706482b94252e68fda4c6391b3/main.py)
## Второй вариант формирования таблицы
* ***A[i][j] == (N/M * i * j) * 2***

```python
  mat = [[0] * strin_len for i in range(col_len)]
  for i in range(col_len):
      for k in range(strin_len):
          if i == 0 and k == 0:
              mat[i][k] = 0
          else:
              mat[i][k] = int((strin_len/col_len*i*k)*2)
```
### Для запуска программы со вторым формированием таблицы нужно запустить файл [main2.py](https://github.com/ThisisFinee/Algo1_lab/blob/ee4f9a06513449706482b94252e68fda4c6391b3/main2.py)
---
# Код реализации алгоритмов
---
## Поиск лесенкой

```python
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
```
### Сложность: O(M+N)
### Алгоритм находится в файле [ladder_search.py](https://github.com/ThisisFinee/Algo1_lab/blob/ee4f9a06513449706482b94252e68fda4c6391b3/ladder_search.py)
### Идея реализации: 
  #### Начальная позиция - правый верхний угол, если элемент поиска больше выбранного, то делаем шаг вниз по матрице, если элемент поиска меньше, то делаем шаг влево по матрице. Действуем таким образом либо пока не пройдём по всем строкам или столбцам, либо пока не найдём элемент.
---
## Двоичный поиск

```python
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
```
### Сложность: O(M*log(N))
### Алгоритм находится в файле [bisec_search.py](https://github.com/ThisisFinee/Algo1_lab/blob/ee4f9a06513449706482b94252e68fda4c6391b3/bisec_search.py)
### Идея реализации:
  #### Прогоняем построчно матрицу следующим алгоритмом: создаём три позиции low = начало массива, high = его конец, mid = (low+high)/2. Если элемент поиска больше элемента с индексом mid, то low=mid+1 и пересчитываем mid, если меньше high = mid-1 и пересчитываем mid, и так до тех пор пока low<high. Если элемент с индексом low равен элементу поиска, то возвращаем его в ином случае возвращаем, что элемент не был найден.
---
## Экспоненциальный поиск
```python
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
```
### Сложность: O(M*log(N))
> #### Бинарый поиск(для экспоненциального)
> ```python
> def bis_search(lst, start, stop, item):
>    mid = (start + stop) // 2
>    if start > stop:
>        return [-1, start]
>    if item == lst[mid-1]:
>        return [1, mid]
>    elif item < lst[mid-1]:
>        return bis_search(lst, start, mid - 1, item)
>    else:
>        return bis_search(lst, mid + 1, stop, item)
> ```
### Оба алгоритма находятся в файле [exp_search.py](https://github.com/ThisisFinee/Algo1_lab/blob/ee4f9a06513449706482b94252e68fda4c6391b3/exp_search.py)
### Идея реализации: 
  #### Начинаем с правого верхнего угла и идём лесенкой(идём вниз если значение поиска больше, идём влево если значение поиска меньше(изменяем только шаги по строке)), увеличивая шаг в 2 раза каждый раз до тех пор пока выбранное значение не будет меньше значения поиска, как только данное условие выполняется прогоняем бинарный поиск по оставшемуся отрезку.
---
# Код замера и вывода времени работы алгоритмов
---
## Поиск лесенкой

```python
start_time1 = time.process_time()
for k in range(1000):
    lad_res = ladder_search(mat, strin_len, col_len, target)
end_time1 = time.process_time()
lad_res.append((end_time1 - start_time1))
if lad_res[0] == -1:
    print(f"{j}.В результате поиска лесенкой элемент не был найден, время: {lad_res[3]}")
else:
    print(f"{j}.Поиск лесенкой.Элемент:{lad_res[0]}, строка:{lad_res[1]+1}, столбец:{lad_res[2]}, время:{lad_res[3]}")
```

### Разъеснение: Каждый алгоритм приходилось запускать 1000 раз, так как в ином случае измерить время было бы просто невозможно(оно всегда равнялось 0)
---
## Двоичный поиск

```python
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
    print(f"{j}.Двоичный поиск.Элемент:{bis_res[0]}, cтрока:{bis_res[1]+1}, cтолбец:{bis_res[2]}, время:{bis_res[3]}")
```
---
## Экспоненциальный поиск

```python
start_time3 = time.process_time()
for i in range(1000):
    exp_res = exp_search(mat, col_len, strin_len, target)
end_time3 = time.process_time()
if exp_res[0] != -1:
    exp_res.insert(0, mat[exp_res[0]][exp_res[1]-1])
exp_res.append(end_time3 - start_time3)
if exp_res[0] == -1:
    print(f"{j}.В результате экспоненциального поиска элемент не был найден, время: {exp_res[1]}")
else:
    print(f"{j}.Экспоненциальный поиск.Элемент:{exp_res[0]}, строка:{exp_res[1]+1}, столбец:{exp_res[2]-1}, время:{exp_res[3]}")
```

### Разъеснение второй цикл в двоичном поиске прогоняет строки матрицы через алгоритм

---
# Таблицы и графики замеров
---
## Первый вариант формирования матрицы

* Таблица(Данные представлены в секундах)

![image1](https://github.com/ThisisFinee/Algo1_lab/blob/8318b3a7f6e895fff568a6101cce6fc1a7e2886e/%D0%9F%D0%BE%D0%B8%D1%81%D0%BA%20%D0%B2%D0%B0%D1%801.png)

* График

![image2](https://github.com/ThisisFinee/Algo1_lab/blob/55a6f52bede988f5a9e388be8ee5e48a92f3b016/%D0%BF%D0%BE%D0%B8%D1%81%D0%BA%20%D0%B2%D0%B0%D1%801-%D0%B3%D1%80%D0%B0%D1%84%D0%B8%D0%BA.png)

## Итог: На маленьких данных поиск лесенкой самый неэффективный, однако при увелечении матрицы его эффективность в сравнении с остальными сильно выше(самый эффективный на маленьких данных экспоненциальный), самый долгий на больших данных двоичный

---

## Второй вариант формирования матрицы

* Таблицы(данные представлены в секундах)

![image3](https://github.com/ThisisFinee/Algo1_lab/blob/55a6f52bede988f5a9e388be8ee5e48a92f3b016/%D0%9F%D0%BE%D0%B8%D1%81%D0%BA%20%D0%B2%D0%B0%D1%802.png)

* График

![image4](https://github.com/ThisisFinee/Algo1_lab/blob/55a6f52bede988f5a9e388be8ee5e48a92f3b016/%D0%9F%D0%BE%D0%B8%D1%81%D0%BA%20%D0%B2%D0%B0%D1%802%20-%20%D0%B3%D1%80%D0%B0%D1%84%D0%B8%D0%BA.png)

## Итог: На маленьких данных всё также самый неэффективный лесенкой и также при увелечении матрицы его эффективность в сравнении с другими повышается(на маленьких данных двоичный и экспоненциальный поиск практически одинаковы, однако эксп всё таки немного быстрее), самый долгий на больших данных двоичный

---

# Итог: Для работы с небольшими матрицами лучше всего подойдёт экспоненциальный или двоичный(эксп быстрее), для больших же матриц гораздо выгоднее использовать поиск лесенкой
