# 1.Написать программу вычисления арифметического выражения заданного строкой. Используются операции +,-,/,*. приоритет операций стандартный. Функцию eval не использовать!
# Пример: 2+2 => 4; 1+2*3 => 7; 1-2*3 => -5;
# Дополнительно: Добавить возможность использования скобок, меняющих приоритет операций. 
# Пример: 1+2*3 => 7; (1+2)*3 => 9;

# operators = {'-': (lambda x,y: float(x)-float(y)),
#              '+': (lambda x,y: float(x)+float(y)),
#              '/': (lambda x,y: float(x)/float(y)),
#              '*': (lambda x,y: float(x)*float(y)) }

# user_expression = '(1+2)*3 ='
# def list_expression(expression):
#     expression_list = []
#     for i in expression:
#         expression_list.append(i)
#     print(expression_list)
#     new_expression_list = []
#     value = ''
#     for i in range(len(expression_list)):
#         if expression_list[i].isdigit():
#             value+= expression_list[i]
#         else:
#             new_expression_list.append(value)
#             new_expression_list.append(expression_list[i])
#             value = ''
#         if(i == len(expression_list)-1):
#             new_expression_list.append(value)
#             expression_list = []
#     for i in range(len(new_expression_list)):
#         if new_expression_list[i]!='' and new_expression_list[i]!=' ' and new_expression_list[i]!='=' :
#             expression_list.append(new_expression_list[i]) 
#     print(expression_list)
#     return expression_list

# user_expression = list_expression(user_expression)

# def calculation(expression, operators):
#     result = []
#     for el in expression:
#         for key in operators:
#             if key in expression:
#                 index = expression.index(key)
#                 result.append(expression[index-1])
#                 result.append(expression[index])
#                 result.append(expression[index+1])
#                 res = operators[key](float(result[0]),float(result[2]))
#                 result.pop(index+1)
#                 result[index] = res
#                 result.pop(index-1)
#                 return result

# def calc_if_bracket(expression):
#     for el in range(len(expression)):
#             if expression[el] == ')':
#                 index2 = el
#                 while expression[el]!= '(':
#                     el-=1
#                 index1 = el
#                 temp = expression[index1+1:index2]
#                 res = calculation(temp,operators)
#                 expression[index1:index2+1]=res
#                 return expression


# while ')' in user_expression:
#     user_expression = calc_if_bracket(user_expression)
# print(user_expression)
# answer = calculation(user_expression,operators)
# print(answer)


#  Реализовать RLE алгоритм. реализовать модуль сжатия и восстановления данных. 
# Входные и выходные данные хранятся в отдельных файлах (в одном файлике отрывок из 
# какой-то книги, а втором файлике — сжатая версия этого текста). 

text = 'AAAAAAAAAVVVVRRREDFGGGG.'
def rle_pres(data):
    code = ''
    char = ''
    count = 1
    for i in data:
        if i != char:
            if char:
                code += str(count) + char
            count = 1
            char = i
        else:
            count += 1
    else:
        code += str(count) + char
    return code

pac_data = rle_pres(text)
print(pac_data)

def rle_unpack(data):
    decode = ''
    count = ''
    for char in data:
        if char.isdigit():
             count += char
        else:
             decode += char * int(count)
             count = ''
    return decode
unpac_data = rle_unpack(pac_data)
print(unpac_data)



# 3 -  ROT13 - это простой шифр подстановки букв, который заменяет букву буквой, которая идет через 13 букв после нее в алфавите. ROT13 является примером шифра Цезаря.
# Создайте функцию, которая принимает строку и возвращает строку, зашифрованную с помощью Rot13. Если в строку включены числа или специальные символы, они должны быть возвращены как есть.
# Также создайте функцию, которая расшифровывает эту строку обратно (некий начальный аналог шифрования сообщений).
# Не использовать функцию encode

# def rot13(text):
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     res = ""
#     for char in text:
#         if char in alphabet:
#             res = res + alphabet[(alphabet.index(char) + 13) % 26]
#         else:
#             res = res + char
#     return res

# text = 'Hail to the Caesar!'
# code = rot13(text)
# print(code)
# encode = rot13(code)
# print(encode)