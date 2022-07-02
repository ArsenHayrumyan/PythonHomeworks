# '''Slide - 1.Calculator'''

# def calc(x, symb, y):
#     if symb == '+':
#         return x + y
#     elif symb == '-':
#         return x - y
#     elif symb == '*':
#         return x * y
#     elif symb == '/':
#         return x / y
# print(calc(int(input('Enter number 1: ')), input('Enter operation symbol: '), int(input('Enter number 2: '))))

# ----------------------------------------------------------------------

# '''Slide - 2.Max of 2 numbers'''

# def func(x, y):

#     if x > y:
#         return 'x is max'
#     elif y > x:
#         return 'y is max'
#     else:
#         return 'Equal!'

# print(func(int(input('Enter number1-->')), int(input('Enter number2-->'))))

# ----------------------------------------------------------------------
# 
# # '''Slide - 3.Sum of all numbers'''

# def func(mylist, sum):
#     for i in mylist:
#         sum += i
#     return sum
# print(func([4, 7, 8, 5, 2], 0))

# ----------------------------------------------------------------------

# '''Slide - 4.Multiply of all numbers'''

# def func(mylist, res):
#     for i in mylist:
#         res *= i
#     return res
# print(func([4, 7, 8, 5, 2], 1))

# ----------------------------------------------------------------------

# '''Slide - 5.Number of digits and letters'''

# def func(str):
#     dig = 0
#     alp = 0
#     for i in str:
#         if i.isdigit():
#             dig += 1
#         elif i.isalpha():
#             alp += 1
#     return dig, alp
# print(func(input('Enter text: ')))

# ----------------------------------------------------------------------

# '''Slide - 6.Ages ?????''' 

# def ages(a, b, c):
#     mylist = [a, b, c]
#     for i in mylist:
#         if i < 16:
#             return 'Too young!'
#     else:
#         return 'Get ready!'

# age1 = int(input('Enter age: '))
# age2 = int(input('Enter age: '))
# age3 = int(input('Enter age: '))

# print(ages(age1, age2, age3))

# ----------------------------------------------------------------------

# '''85. Вычисляем длину гипотенузы'''

# def tri(a, b):
#     c = ((a ** 2) + (b ** 2)) ** 0.5
#     return round(c, 2)

# a_side = float(input('Enter the lenght of first side of triangle: '))
# b_side = float(input('Enter the lenght of second side of triangle: '))

# print(f'The lenght of hypotenuse = {tri(a_side, b_side)}')

# ----------------------------------------------------------------------

# '''86. Плата за такси'''

# def taxi(x):
#     sum = 4 + (x * 1000 / 140 * 0.25)
#     return round(sum, 2)
# print(taxi(int(input('Enter distance: '))))

# ----------------------------------------------------------------------

# '''87. Расчет стоимости доставки'''

# def delivery(n):
#     sum = 10.95 + ((n - 1) * 2.95)
#     return sum
# items = int(input('Enter the count of items of your delivery: '))
# print(f'Amount of your order delivery = ${delivery(items)}')

# ----------------------------------------------------------------------

# '''88. Медиана трех значений'''

# def med(x, y, z):
#     if x > y > z or x < y < z:
#         return y
#     elif x > z > y or x < z < y:
#         return z
#     elif y > x > z or y < x < z:
#         return x
    
# num1 = int(input('Enter first number: '))
# num2 = int(input('Enter second number: '))
# num3 = int(input('Enter third number: '))

# print(f'Mediana of entered numbers is {med(num1, num2, num3)}')

# ----------------------------------------------------------------------

# '''89. Переводим целые числа в числительные'''

# def num(n:int):
#     if n < 1 or n >12:
#         pass
#     elif n == 1:
#         return 'First'
#     elif n == 2:
#         return 'Second'
#     elif n == 3:
#         return 'Third'
#     elif n == 4:
#         return 'Fourth'
#     elif n == 5:
#         return 'Fifth'
#     elif n == 6:
#         return 'Sixth'
#     elif n == 7:
#         return 'Seventh'
#     elif n == 8:
#         return 'Eighth'
#     elif n == 9:
#         return 'Ninth'
#     elif n == 10:
#         return 'Tenth'
#     elif n == 11:
#         return 'Eleventh'
#     elif n == 12:
#         return 'Twelfth'

# for i in range (1, 13):
#     print(num(i))

# ----------------------------------------------------------------------

# '''90. Двенадцать дней Рождества'''

# def day(d:int):
#     print(f'On the {num(d)} day of Christmas\nmy true love sent to me:')
#     if d < 1 or d > 12:
#         pass

#     if d >= 12:
#         print('Twelve drummers drumming')
#     if d >= 11:
#         print('Eleven pipers piping')
#     if d >= 10:
#         print('Ten lords a-leaping')
#     if d >= 9:
#         print('Nine ladies dancing')
#     if d >= 8:
#         print('Eight maids a-milking')
#     if d >= 7:
#         print('Seven swans a-swimming')
#     if d >= 6:
#         print('Six geese a-laying')
#     if d >= 5:
#         print('Five golden rings')
#     if d >= 4:
#         print('Four calling birds')
#     if d >= 3:
#         print('Three french hens')
#     if d >= 2:
#         print('Two turtle doves, and')
#     if d >= 1:
#         print('A partridge in a pear tree.\n')

# for k in range(1, 13):
#     day(k)

# ----------------------------------------------------------------------

# '''91. Григорианский календарь в порядковый'''

# def cal(d, m, y):
#     if y % 4 == 0:
#         days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     else:
#         days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     day_count = 0
#     for i in range(m - 1):
#         day_count += days[i]
#     return day_count + d
# date_d = int(input('Enter day: '))
# date_m = int(input('Enter month: '))
# date_y = int(input('Enter year: '))
# print(f'Ordinal date of your entered day is {cal(date_d, date_m, date_y)}th day of {date_y}')

# ----------------------------------------------------------------------

# '''93. Центрируем строку'''

# def cent(str, w):
#     if len(str) >= w:
#         return str
#     else:
#         return ((w - len(str)) // 2) * ' ' + str + ((w - len(str)) // 2) * ' '

# for i in range(4):
#     s = input('Enter text: ')
#     window = int(input('Enter the width: '))
#     print(cent(s, window))

# ----------------------------------------------------------------------

# '''94. Треугольник ли?'''

# def tr(a, b, c):
#     if a <= 0 or b <= 0 or c <= 0:
#         return False
#     if a + b <= c or a + c <= b or b + c <= a:
#         return False
#     else:
#         return True

# a_side = int(input('Enter first side of possible triangle: '))
# b_side = int(input('Enter second side of possible triangle: '))
# c_side = int(input('Enter third side of possible triangle: '))

# if tr(a_side, b_side, c_side):
#     print('Making triangle with your entered parameters is possible.')
# else:
#     print('Making triangle with your entered parameters is impossible.')

# ----------------------------------------------------------------------

# '''96. Является ли строка целым числом?'''

# def dig(s):
#     mylist = []
#     for i in s:
#         if i != ' ':
#             mylist.append(i)
#     count = 0
#     for i in mylist:
#         if i.isdigit():
#             count += 1
#     if count == len(mylist):
#         return True
#     else:
#         return False

# str = input('Enter text: ')
# print(dig(str))

# ----------------------------------------------------------------------

# '''98. Простое число?'''

# def ord_num(n:int):
#     mylist = []
#     for i in range(2, n + 1):
#         for j in range(2, i):
#             if i % j == 0:
#                 break
#         else:
#             mylist.append(i)
#     return n in mylist

# print(ord_num(int(input('Enter number to check: '))))

# ----------------------------------------------------------------------

# '''99. Следующее простое число'''

# def ord_num(n:int):
#     mylist = []
#     for i in range(2, (n + 1) * 2):
#         for j in range(2, i):
#             if i % j == 0:
#                 break
#         else:
#             if i > n:
#                 mylist.append(i)
#     return mylist[0]

# print(ord_num(int(input('Enter number to check: '))))

# ----------------------------------------------------------------------

# '''101. Случайный номерной знак'''

# import random

# def car_num():
#     letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     num = ''
#     let = ''
#     for i in range(4):
#         num += str(random.randint(0, 9))
#     for i in range(3):
#         let += random.choice(letters)
#     return num + '-' + let
# print(f'Your car number is {car_num()}. Congratulations!')

# ----------------------------------------------------------------------

# '''102. Проверка пароля на надежность'''

# def your_pass(s):
#     upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#     symb = ['!', '@', '#', '$', '%', '&', '*']
#     dig = 0
#     symb_count = 0
#     for i in s:
#         if i.isdigit():
#             dig +=1
#         elif i in symb:
#             symb_count += 1
        
#     return len(s) > 8 and s[0] in upper and dig >= 1 and symb_count >= 1

# print(your_pass(input('Enter password: ')))

# ----------------------------------------------------------------------

# '''104. Шестнадцатеричные и десятичные числа'''

# def hextoint(H):
#     mydict = {
#         10: 'A',
#         11: 'B',
#         12: 'C',
#         13: 'D',
#         14: 'E',
#         15: 'F'
#     }
#     for i in mydict:
#         if H == mydict[i]:
#             return i
#     if int(H) in range(0, 10):
#         return H
#     else:
#         return 'ERROR'
# HEX = input('Enter value in HEX: ')
# print(f'The decimal eq.of your HEX value = {hextoint(HEX)}')

# def inttohex(I):
#     mydict = {
#         10: 'A',
#         11: 'B',
#         12: 'C',
#         13: 'D',
#         14: 'E',
#         15: 'F'
#     }
#     for i in mydict:
#         if int(I) == i:
#             return mydict[i]
#     if int(I) in range(0, 10):
#         return I
#     else:
#         return 'ERROR'
# INT = input('Enter value in decimal: ')
# print(f'The HEX eq.of your decimal value = {inttohex(INT)}')

# ----------------------------------------------------------------------

# '''106. Дни в месяце'''

# def days(m, y):
#     m31 = (1, 3, 5, 7, 8, 10 ,12)
#     if m in m31:
#         return 'This month has 31 days.'
#     elif m <= 12 and m != 2:
#         return 'This month has 30 days.'
#     elif m == 2 and y % 4 == 0:
#         return 'This month has 29 days.'
#     elif m == 2 and y % 4 != 0:
#         return 'This month has 28 days.'
#     else:
#         return 'You entered the wrong format.'

# print (days(int(input('Enter month: ')), int(input('Enter year: '))))

# ----------------------------------------------------------------------
    
# '''107. Максимальное сокращение дробей'''

# def func(x, y):
#     list_x = []
#     list_y = []
#     max_del = None
#     for i in range(1, x + 1):
#         if x % i == 0:
#             list_x.append(i)
#     for i in range(1, y + 1):
#         if y % i == 0:
#             list_y.append(i)
#     for i in list_x:
#         for j in list_y:
#             if i == j:
#                 max_del = i
#                 break
#     return int(x / max_del), int(y / max_del)
# num1 = int(input('Enter num1: '))
# num2 = int(input('Enter num2: '))
# print(func(num1, num2))

# ----------------------------------------------------------------------

# '''108. Переводим меры'''

# def weight(x:int, s:str) -> str:
#     tea = None
#     table = None
#     cup = None

#     if s == 'cup':
#         return str(x) + ' ' + s
#     elif s == 'tablespoon':
#         cup = x // 16
#         table = x % 16
#         return str(int(cup)) + ' cup,' + ' ' + str(int(table)) + ' tablespoon'
#     elif s == 'teaspoon':
#         cup = (x / 3) // 16
#         table = (x - (cup * 16 * 3)) // 3
#         tea = (x - (cup * 16 * 3)) % 3
#         return str(int(cup)) + ' cup,' + ' ' + str(int(table)) + ' tablespoon,' + ' ' + str(int(tea)) + ' teaspoon'
# print(weight(int(input('Enter amount: ')), input('Enter measure unit: ')))

# ----------------------------------------------------------------------

# '''109. Магические даты'''

# def magdate(d, m, y):
#     if d * m == y % 100:
#         return 'Date is magic'
#     else:
#         return 'Date is ordinary'

# # day = int(input('Enter day: '))
# # month = int(input('Enter month: '))
# # year = int(input('Enter year: '))

# # print(magdate(day, month, year))

# def days(m, y):
#     m31 = (1, 3, 5, 7, 8, 10 ,12)
#     if m in m31:
#         return 31
#     elif m <= 12 and m != 2:
#         return 30
#     elif m == 2 and y % 4 == 0:
#         return 29
#     elif m == 2 and y % 4 != 0:
#         return 28
#     else:
#         return 'You entered the wrong format.'

# def magdate(d, m, y):
#     if d * m == y % 100:
#         return f'{d} : {m} : {y}'
#     else:
#         pass
        

# for year in range(1900, 2000):
#     for month in range(1, 13):
#         for day in range(1, days(month, year) + 1):
#             if magdate(day, month, year):
#                 print(magdate(day, month, year))
            
# ----------------------------------------------------------------------


