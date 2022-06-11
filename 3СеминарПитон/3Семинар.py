# 1.Найти НОК двух чисел

# def NOD(a,b): # для вычисления НОК потребуется найти наибольший общий делитель(НОД)
#     while a != b: 
#         if a > b:
#             a = a - b
#         else:
#             b = b - a        
#     return(a)
# def NOK(a,b):
#     return(a*b//NOD(a,b))

# value1 = int(input('Введите первое число: '))
# value2 = int(input('Введите второе число: '))
# print(f'НОД = {NOK(value1,value2)}')

# 2.Вычислить число Пи c заданной точностью d
#   Пример: при d = 0.001,  c= 3.141. 

# import math

# d = 0.001
# pi =48*math.atan(1/18)+32*math.atan(1/57)-20*math.atan(1/239) # Формула Гаусса
# accuracy = int(len(str(d).split(".")[1]))
# pi = str(pi)
# print(pi[:accuracy+2])


# 3.Составить список простых множителей натурального числа N

# def primefactors(N):
#     if N == 1: return [1]
#     list_primefactors = []
#     i = 2
#     while N != 1:
#         if N % i == 0:
#             N = N // i
#             list_primefactors.append(i)
#             continue
#         i+=1
#     return list_primefactors
        
# numberN = int(input('ВВедите натуральное число N: '))
# print(primefactors(numberN))


# 4.Дана последовательность чисел. Получить список неповторяющихся элементов исходной последовательности
#  Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]

# my_list = [1, 2, 3, 5, 1, 5, 3, 10]
# my_set = set(my_list)
# new_list = list(my_set)
# print(f'{my_list} => {new_list}')


# 5.Дан текстовый файл, содержащий целые числа. Удалить из него все четные числа. 
 
# from random import randint, random

# with open ('file.txt','w') as data:
#     size = 10
#     for i in range(size):
#         sep = ' ' if i !=  size - 1 else ''
#         data.write(str(randint(-10, 10)) + sep)
    
# with open ('file.txt', 'r') as data:
#     data = map(int, data.read().split(' '))
#     data_list = list(filter(lambda x: x % 2, data))
#     data_new = ' '.join(map(str, data_list))

# with open ('file.txt','a') as data:
#     data.write(f'\n{data_new}')
