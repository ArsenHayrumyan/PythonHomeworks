# '''149. Отображаем начало файла'''

# def func(file:str, n:int, mylist:list=[]) -> str:
#     with open(file, 'rt') as x:
#         res = x.readlines()
#     for i in res[:n]:
#         i = i.replace('\n', '')
#         mylist.append(i)
#     for i in mylist:
#         print(i)

# func('test.txt', 4)

# ----------------------------------------------

# '''150. Отображаем конец файла'''

# def func(file:str, n:int, mylist:list=[]) -> str:
#     with open(file, 'rt') as x:
#         res = x.readlines()
#     for i in res[-n:]:
#         i = i.replace('\n', '')
#         mylist.append(i)
#     for i in mylist:
#         print(i)

# func('test.txt', 4)

# ----------------------------------------------

# '''151. Сцепляем файлы'''

# def con(file1, file2):
#     with open(file2, 'rt') as x:
#         res = x.readlines()
#     with open(file1, 'a') as y:
#         y.write('\n')
#         for i in res:
#             y.write(i)

# con('test1.txt', 'test2.txt')

# ----------------------------------------------

# '''152. Нумеруем строки в файле'''

# def num(file1, file2):
#     with open(file1, 'rt') as x:
#         res = x.readlines()
#     for i in range(len(res)):
#         res[i] = str(i + 1) + ': ' + res[i]
#     with open(file2, 'w') as y:
#         for i in res:
#             y.write(i)
# num('num1.txt', 'num2.txt')

# ----------------------------------------------

# '''153. Самое длинное слово в файле'''

# with open('longest_word.txt', 'rt') as f:
#     res = f.readlines()
#     word = ''
#     mylist = []
#     for i in res:
#         i = i.replace('\n', '')
#         for j in i:
#                 word += j
#                 mylist.append(word)
#                 word = ''
#     str = ''.join(mylist)
#     newlist = str.split(' ')
#     newlist.sort(key=len, reverse=True)
#     print(f'The longest word in text is \"{newlist[0]}\" and has {len(newlist[0])} characters')
#     for k in range(1, len(newlist)):
#         if len(newlist[k]) == len(newlist[0]):
#             print(f'The next longest word in text with {len(newlist[0])} characters is \"{newlist[k]}\"') 

# ----------------------------------------------

# '''154. Частота букв в файле'''

# def char(a:str):
#     count = 0
#     with open('longest_word.txt', 'rt') as x:
#         res = x.read()
#         for i in res:
#             if i.lower() == a.lower():
#                 count += 1
#         return count
            
        
# letter = input('Enter letter to count: ')
# while len(letter) > 1 or letter.isdigit():
#     print('You must enter only a letter.')
#     letter = input('Please, try again: ')
# print(f'There are {char(letter)} \"{letter}\" in text.')

# ----------------------------------------------

# '''155. Частота слов в файле'''

# def word(s:str):
#     with open('longest_word.txt', 'rt') as f:
#         res = f.readlines()
#         word = ''
#         mylist = []
#         for i in res:
#             i = i.replace('\n', '')
#             for j in i:
#                     word += j
#                     mylist.append(word)
#                     word = ''
#         str = ''.join(mylist)
#         newlist = str.split(' ')
#         count = 0
#         for i in newlist:
#             if s.lower() == i.lower():
#                 count += 1
#         return count

# myword = input('Enter word to count: ')
# while len(myword) < 1 or myword.isdigit() or ' ' in myword:
#     print('You must enter only a word.')
#     myword = input('Please, try again: ')
# print(f'There are {word(myword)} \"{myword}\" in text.')



            
    

