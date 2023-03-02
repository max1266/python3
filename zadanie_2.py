# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
import random

n = int(input('введите число N: '))
list_1 = []
for i in range(n):
    list_1.append(random.randint(1,n))
print(list_1)    
x = int(input('Ведите число для поиска :'))
result = ''
for i in range(n):
    if list_1[i] == x +1 or list_1 == x - 1:
        result = list_1[i]
        break
print(list_1[i])

