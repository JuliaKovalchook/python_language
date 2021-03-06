﻿#task1------------------------------------------------------------
"""
Найдите индексы первого вхождения максимального элемента. Выведите два числа: номер строки и номер столбца, в которых стоит наибольший элемент в двумерном массиве. Если таких элементов несколько, то выводится тот, у которого меньше номер строки, а если номера строк равны то тот, у которого меньше номер столбца.
Программа получает на вход размеры массива n и m, затем n строк по m чисел в каждой.
"""


n, m = [int(i) for i in input().split()]
a = [[int(j) for j in input().split()] for i in range(n)]
max_s, max_l=0,0
max=a[0][0]
for i in range(n):
    for j in range(m):
        if a[i][j] > max:
            max = a[i][j]
            max_s,max_l=i,j
print(max_s, max_l)

#task2------------------------------------------------------------
"""
Дано нечетное число n. Создайте двумерный массив из n×n элементов, заполнив его символами "."(каждый элемент массива является строкой из одного символа). Затем заполните символами "*" среднюю строку массива, средний столбец массива, главную диагональ и побочную диагональ. В результате единицы в массиве должны образовывать изображение звездочки. Выведите полученный массив на экран, разделяя элементы массива пробелами.
"""


n = int(input())
a = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        if i==j:
            a[i][j] = "*"
        elif i+j==n-1:
            a[i][j] = "*"
        elif j==n//2:
            a[i][j] ="*"
        elif i==n//2:
            a[i][j] ="*"
        else:
            a[i][j] ="." 
    
        
for row in a:
    print(' '.join([str(elem) for elem in row]))

#task3------------------------------------------------------------
"""
Даны два числа n и m. Создайте двумерный массив размером n×m и заполните его символами "." и "*" в шахматном порядке. В левом верхнем углу должна стоять точка.
"""


n, m = [int(i) for i in input().split()]
a=[["*"] * m for i in range(n)]
for i in range(n):
    for j in range(m):
        if i%2==1:
            if j%2==1:
                a[i][j] = "."
        elif i%2==0:
            if j%2==0:
                a[i][j] = "."
for row in a:
    print(' '.join([str(elem) for elem in row]))

#task4------------------------------------------------------------
"""
Дано число n. Создайте массив размером n×n и заполните его по следующему правилу. На главной диагонали должны быть записаны числа 0. На двух диагоналях, прилегающих к главной, числа 1. На следующих двух диагоналях числа 2, и т.д.
"""


n = int(input())
a = [[0] * n for i in range(n)]
for j in range(n):
    for i in range(n):
        a[i][j] = abs(i - j)

for row in a:
    print(' '.join([str(elem) for elem in row]))

#task5------------------------------------------------------------
"""
Дано число n. Создайте массив размером n×n и заполните его по следующему правилу:
Числа на диагонали, идущей из правого верхнего в левый нижний угол равны 1.
Числа, стоящие выше этой диагонали, равны 0.
Числа, стоящие ниже этой диагонали, равны 2.
Полученный массив выведите на экран. Числа в строке разделяйте одним пробелом.
"""


n = int(input())
a =[[0] * n for i in range(n)] 
for i in range(n):
    for j in range(n):
        if i + j < n - 1:
            a[i][j] = 0
        elif i + j == n - 1:
            a[i][j] = 1
        elif i + j > n - 1:
            a[i][j] = 2
for i in a:
    print(' '.join(str(j) for j in i))

#task6------------------------------------------------------------
"""
Дан двумерный массив и два числа: i и j. Поменяйте в массиве столбцы с номерами i и j и выведите результат.
Программа получает на вход размеры массива n и m, затем элементы массива, затем числа i и j.
"""


n, m = [int(i) for i in input().split()]
a = [[int(j) for j in input().split()] for i in range(n)]
i, j = [int(i) for i in input().split()]
for x in range(n):
    a[x][i],a[x][j] = a[x][j],a[x][i]
for row in a:
    print(' '.join([str(a) for a in row]))
