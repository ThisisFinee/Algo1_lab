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
### Для запуска программы с первым формированием таблицы нужно запустить файл [main.py](https://github.com/ThisisFinee/Algo1_lab/blob/643d6d3e70b80330760eb312f585129d788da906/main.py)
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
### Для запуска программы со вторым формированием таблицы нужно запустить файл [main2.py](https://github.com/ThisisFinee/Algo1_lab/blob/643d6d3e70b80330760eb312f585129d788da906/main2.py)
---
# Код реализации алгоритмов
---
## Поиск лесенкой

```python
def ladder_search(a, m, n, el):
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
```
### Сложность: O(M+N)
### Алгоритм находится в файле [ladder_search.py](https://github.com/ThisisFinee/Algo1_lab/blob/643d6d3e70b80330760eb312f585129d788da906/ladder_search.py)
### Идея реализации: 
  #### Начальная позиция - правый верхний угол, если элемент поиска больше выбранного, то делаем шаг вниз по матрице, если элемент поиска меньше, то делаем шаг влево по матрице. Действуем таким образом либо пока не пройдём по всем строкам или столбцам, либо пока не найдём элемент.
---
## Двоичный поиск

```python
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
```
### Сложность: O(M*log(N))
### Алгоритм находится в файле [bisec_search.py](https://github.com/ThisisFinee/Algo1_lab/blob/643d6d3e70b80330760eb312f585129d788da906/bisec_search.py)
### Идея реализации:
  #### Прогоняем построчно матрицу следующим алгоритмом: создаём три позиции low = начало массива, high = его конец, mid = (low+high)/2. Если элемент поиска больше элемента с индексом mid, то low=mid+1 и пересчитываем mid, если меньше high = mid-1 и пересчитываем mid, и так до тех пор пока low<high. Если элемент с индексом low равен элементу поиска, то возвращаем его в ином случае возвращаем, что элемент не был найден.
---
## Экспоненциальный поиск
```python
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
```
### Сложность: O(M*log(N))
> #### Бинарый поиск(для экспоненциального)
> ```python
> def bis_search(lst, item):
>    low, high = 0, len(lst)
>    while low < high:
>        mid = (low + high) // 2
>        mid_val = lst[mid]
>        if item > mid_val:
>            low = mid + 1
>        else:
>            high = mid - 1
>    if low == len(lst):
>        low -= 1
>    if lst[low] == item:
>        return [lst[low]]
>    else:
>        return [-1]
> ```
### Оба алгоритма находятся в файле [exp_search.py](https://github.com/ThisisFinee/Algo1_lab/blob/643d6d3e70b80330760eb312f585129d788da906/exp_search.py)
### Идея реализации: 
  #### Проверяем нулевой элемент массива(так как для удобства идём с первого), если он не равен элементу поиска, то запускаем алгоритм, создаём позицию ind = 1, и при каждой итерации цикла умножаем эту позицию на 2(ind *= 2), цикл работает до тех пор пока элемент с индексом ind меньше элемента поиска или пока ind < len(array)(в этом случае проверяем последний элемент массива, если он меньше, то выводим что элемента поиска нет, если он больше то запускаем двоичный поиск на срез массива от ind//2 до len(array)), если же элемент поиска меньше выбранного элемента, то запускаем двоичный поиск от ind//2 до ind, преждевременно переведя все числа в из однмерных значений в двумерные(ind,ind//2 -> [ind//n],[ind%n] and [(ind//2)//n],[(ind//2)%n]
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
    print(f"{j}.Поиск лесенкой.Элемент:{lad_res[0]}, строка:{lad_res[1]}, столбец:{lad_res[2]}, время:{lad_res[3]}")
```

### Разъеснение: Каждый алгоритм приходилось запускать 1000 раз, так как в ином случае измерить время было бы просто невозможно(оно всегда равнялось 0)
---
## Двоичный поиск

```python
start_time2 = time.process_time()
for k in range(1000):
    for m in range(len(mat)):
        bis_res = bisec_search(mat[m], target)
        if bis_res[0] != -1:
            break
end_time2 = time.process_time()
bis_res.append(end_time2 - start_time2)
if bis_res[0] == -1:
    print(f"{j}.В результате двоичного поиска элемент не был найден, время: {bis_res[1]}")
else:
    print(f"{j}.Двоичный поиск.Элемент:{bis_res[0]} был найден, время:{bis_res[1]}")
```
---
## Экспоненциальный поиск

```python
start_time3 = time.process_time()
for i in range(1000):
    exp_res = exp_search(mat, target)
end_time3 = time.process_time()
exp_res.append(end_time3 - start_time3)
if exp_res[0] == -1:
    print(f"{j}.В результате экспоненциального поиска элемент не был найден, время: {exp_res[1]}")
else:
    print(f"{j}.Экспоненциальный поиск.Элемент:{exp_res[0]}, был найден, время:{exp_res[1]}")

```

### Разъеснение второй цикл в двоичном поиске прогоняет строки матрицы через алгоритм

---
# Таблицы и графики замеров
---
## Первый вариант формирования матрицы

* Таблица(Данные представлены в секундах)

![image1](https://github.com/ThisisFinee/Algo1_lab/blob/643d6d3e70b80330760eb312f585129d788da906/%D0%9F%D0%BE%D0%B8%D1%81%D0%BA%20%D0%B2%D0%B0%D1%801.png)

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
