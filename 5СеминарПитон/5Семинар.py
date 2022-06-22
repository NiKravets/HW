# 1.Напишите программу, удаляющую из текста все слова содержащие "абв", которое регистронезависимо.
# Используйте знания с последней лекции. Выполните ее в виде функции. 
# Пример: «абвгдеж рабав копыто фабв Абкн абрыволк аБволк»

# def remove_char_text(text_input, chars):
#     return text_input.replace(chars,"")

# text_input = "абвгдеж рабав копыто фабв Абкн абрыволк аБволк"
# chars = "абв"
# print(text_input.replace(chars,""))


# 2.Вы когда-нибудь играли в игру "Крестики-нолики"? Попробуйте создать её, причем чтобы сыграть в нее можно было в одиночку. 

# board = list(range(1,10))

# def draw_board(board):
#    print("-" * 13)
#    for i in range(3):
#       print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
#       print("-" * 13)

# def take_input(player_token):
#    valid = False
#    while not valid:
#       player_answer = input("Куда поставим " + player_token+"? ")
#       try:
#          player_answer = int(player_answer)
#       except:
#          print("Некорректный ввод. Вы уверены, что ввели число?")
#          continue
#       if player_answer >= 1 and player_answer <= 9:
#          if(str(board[player_answer-1]) not in "XO"):
#             board[player_answer-1] = player_token
#             valid = True
#          else:
#             print("Эта клетка уже занята!")
#       else:
#         print("Некорректный ввод. Введите число от 1 до 9.")

# def check_win(board):
#    win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
#    for each in win_coord:
#        if board[each[0]] == board[each[1]] == board[each[2]]:
#           return board[each[0]]
#    return False

# def main(board):
#     counter = 0
#     win = False
#     while not win:
#         draw_board(board)
#         if counter % 2 == 0:
#            take_input("X")
#         else:
#            take_input("O")
#         counter += 1
#         if counter > 4:
#            tmp = check_win(board)
#            if tmp:
#               print(tmp, "выиграл!")
#               win = True
#               break
#         if counter == 9:
#             print("Ничья!")
#             break
#     draw_board(board)
# main(board)

# input("Нажмите Enter для выхода!")


# 3.Вот вам текст:
# «Ну, вышел я, короче, из подъезда. В общем, короче говоря, шел я, кажется, в магазин.
# Ну,эээ, в общем, было лето, кажется. Как бы тепло. Солнечно, короче. Иду я, иду, в общем, по улице, а тут, короче, яма. 
# Я, эээээ…. Упал в нее. И снова вышел, короче, из подъезда. Ясен пень, в магазин. В общем, лето на дворе, жарко, солнечно, птицы, короче, летают.
# Кстати, иду я по улице, иду, а тут, короче, яма. Ну, я в нее упал, в общем. Вышел из подъезда, короче. Лето на дворе, ясен пень.
# Птицы поют, короче, солнечно. В общем, в магазин мне надо. Что-то явно не так, короче. 
# «Рекурсия», - подумал я. Ээээ...короче, в общем, пошел другой дорогой и не упал в эту… ээээ… яму. Хлеба купил».
# Отфильтруйте его, чтобы этот текст можно было нормально прочесть. Предусмотрите вариант, что мусорные слова могли быть написаны без использования запятых.

# from encodings import utf_8

# parasites = { 1:'«Ну,', 2:'короче.', 3:'короче,',4:'В',5:'общем,',6:'говоря,',7:'кажется,',
#               8:'кажется.', 9:'Ну,эээ,', 10:'Как', 11:'бы', 12:'эээээ….', 13:'Ясен',14:'ясен',
#               15:'пень', 16:'Кстати,', 17:'Ээээ...короче,', 18:'ээээ…', 19:'короче', 20:'пень.',
#               21:'общем.'}

# def parasites_clear(text, dictionary):
#     new_text = text.copy()
#     for i in range (len(text)):
#         for key in dictionary.keys():
#             if text[i] == dictionary[key]:
#                 new_text.remove(text[i])   
#     return new_text

# def capital_letter(text):
#     new_text = list(text)
#     for i in range (len(new_text)):
#         if new_text[i-2] == '.' or i == 0:
#             new_text[i] = new_text[i].upper()
#     return new_text

# with open('task3.txt', 'r', encoding=('utf-8')) as text:
#     bad_text = text.read().split()

# new_text = ' '.join(parasites_clear(bad_text, parasites))
# new_text = new_text.lower()
# new_text = ''.join(capital_letter(new_text))

# print(new_text)  