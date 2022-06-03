import math
from random import randint, random


# Найти сумму чисел списка стоящих на нечетной позиции
# Пример:[1,2,3,4] -> 4

# arr = []
# for x in range(10):
#     arr.append(randint(1,10))
# size = len(arr)
# sum = 0
# for i in range(0, size, 2):
#     sum += arr[i]
# print(f'{arr} -> {sum}')

# Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д. 
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15] 


# size_arr1 = int(input('Введите длинну списка: '))
# arr1 = []
# for x in range(size_arr1):
#     arr1.append(randint(1,10))
# size = math.ceil(size_arr1/2)
# arr2 = []
# for i in range(size):
#     arr2.append((arr1[i])*(arr1[-i-1]))
# print(f'{arr1} => {arr2}')

# В заданном списке вещественных чисел найдите разницу между максимальным и минимальным значением дробной части элементов.
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# arr = [1.1, 1.2, 3.1, 5, 10.01]
# print(arr, end='')
# for i in range(len(arr)):
#     arr[i] = round(arr[i] - int(arr[i]), 2)
# arr.remove(0)
# print(f' => {max(arr)-min(arr)}')

# Написать программу преобразования десятичного числа в двоичное

# numb10 = int(input('Введите целое число: '))
# numb2 = ''
# while numb10 > 0:
#     numb2 = str(numb10 % 2) + numb2
#     numb10 = numb10 // 2
# print(numb2)
