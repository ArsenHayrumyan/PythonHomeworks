# '''173. Сумма значений'''

# def gumar():
#     num = input('Enter number: ')
#     if num == '':
#         return 0.0
#     else:
#         return float(num) + gumar()

# print(gumar())

# ---------------------------------------------

# '''174. Наибольший общий делитель'''

# def Ev(a, b):
#     if b == 0:
#         return a
#     else:
#         c = a % b
#         return Ev(b, c)
# num1 = int(input('Enter number 1: '))
# num2 = int(input('Enter number 2: '))
# print(Ev(num1, num2))

# ---------------------------------------------

# '''175. Рекурсивный перевод числа из десятичного в двоичное'''

# def dec_to_bin(n):
#     s = []
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         res = n % 2
#         s.append(str(res))
#         s.append(str(dec_to_bin(n // 2)))
#         return ''.join(s[::-1])
# dec_num = int(input('Enter positive decimal number for transform to binary: '))
# print(f'Binary equivalent of your entered number is {dec_to_bin(dec_num)}')

# ---------------------------------------------