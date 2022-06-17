# 1.Дан список чисел. Создать список в который попадают числа, описывающие возрастающую последовательность и содержащие максимальное количество элементов. 
#   Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3, 4, 6, 7]
#           [5, 2, 3, 4, 6, 1, 7] => [2, 3, 4, 6, 7]

# import itertools
# from itertools import combinations

# list_number = [1, 5, 2, 3, 4, 6, 1, 7]
# for i in range(len(list_number)-1):
#     possible_comb = list(combinations(list_number, len(list_number)-i))
#     for j in range(len(possible_comb)-1):
#         result = list(possible_comb[j])
#         if result == sorted(result):
#             print(result)


# 2.Создать и заполнить файл случайными целыми значениями. Выполнить сортировку содержимого файла по возрастанию.

# from random import randint

# with open ('file.txt','w') as data:
#     size = 10
#     for i in range(size):
#         sep = ' ' if i !=  size - 1 else ''
#         data.write(str(randint(-100, 101)) + sep)

# with open ('file.txt', 'r') as data:
#     data_list = list(map(int, data.read().split(' ')))
#     data_list = sorted(data_list)
#     data_new = ' '.join(map(str, data_list))

# with open ('file.txt','a') as data:
#     data.write(f'\n{data_new}')


# 3.Вот вам файл с тысячей чисел. https://cloud.mail.ru/public/DQgN/LqoQzPEec
# Задача: найти триплеты и просто выводить их на экран. Триплетом называются три числа, которые в сумме дают 0. 
# (решение будет долгим, ибо является демонстрационным при теме многопоточного программирования). 
   
# def is_tripl(first, second, third):
#     if int(first) + int(second) + int(third) == 0:
#         return True

# with open ('1Kints.txt', 'r') as data:
#     list_numbers = data.read().strip().split()
    

# for i in range(len(list_numbers)):
#     for j in range(len(list_numbers)-1):
#         for k in range(len(list_numbers)-2):
#             if is_tripl(list_numbers[i], list_numbers[j], list_numbers[k]):
#                 print(list_numbers[i], list_numbers[j], list_numbers[k])
 

