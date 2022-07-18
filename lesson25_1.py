# '''1. Function'''

# def list_create(a:int, b:int, step:int) -> list:
#     mylist = []
#     for i in range(a, (b + 1), step):
#         mylist.append(i)
#     return mylist

# num1 = int(input('Enter first number: '))
# num2 = int(input('Enter second number: '))
# step = int(input('Enter step: '))
# print(f'The required list is {list_create(num1, num2, step)}')

# -------------------------------------------------

# '''2. List'''

# def prod(mylist:list[int]) -> list[int]:
#     newlist = []
#     for i in range(len(mylist) - 1):
#         newlist.append(mylist[i] * mylist[i + 1])
#     return newlist

# print(prod([3, 7, 12, 5, 20, 0]))
# print(prod([1, 1, 4, 32, 6]))

# -------------------------------------------------

# '''3. New sentence'''

# def sent(s:str, words:list[str]) -> str:
#     if s.count('_') > len(words):
#         return 'There are more missing words, than you give.'
#     elif s.count('_') < len(words):
#         return 'You give more words than missings.'
#     else:
#         while len(words) > 0:
#             for i in range(len(s)):
#                 if s[i] == '_':
#                     s = s[:i] + words[0] + s[(i + 1):]
#                     words.remove(words[0])
#         return s

# print(sent('_, we have a _.', ['Ashot', 'problems'])) 

# -------------------------------------------------

# '''4. Sum word'''

# def sum_word(mylist:list[str]) -> int:
#     mylist.sort(key=len)
#     return len(mylist[0]) + len(mylist[-1])

# words = ['anymore', 'raven', 'me', 'communicate']
# print(sum_word(words))

# -------------------------------------------------

# '''5. Find index'''

# def ind(mylist:list, num:int):
#     if num in mylist:
#         return mylist.index(num)
#     else:
#         new = mylist.copy()
#         new.sort()
#         big = []
#         small = []
#         for i in new:
#             if i < num:
#                 small.append(i)
#             elif i > num:
#                 big.append(i)
#         if num - small[-1] < big[0] - num:
#             return mylist.index(small[-1])
#         elif num - small[-1] > big[0] - num:
#             return mylist.index(big[0])
#         else:
#             return mylist.index(big[0])

# print(ind([21, -9, 15, 2116, -71, 33], -71))
# print(ind([ 36, -12, 47, -58, 148, -55, -19, 10], -56))

# -------------------------------------------------

# '''6. New dict'''

# def new_dict(N:int) -> dict:
#     mydict = {i:i ** 2 for i in range(1, N + 1)}
#     return mydict

# num = int(input('Enter number for range: '))
# print(new_dict(num))

# -------------------------------------------------

# '''7. Invert dict'''

# def func(mydict:dict[str:int], newdict:dict={}) -> dict[int:str]:
#     for i in mydict:
#         if mydict[i] not in newdict:
#             newdict[mydict[i]] = [i]
#         else:
#             newdict[mydict[i]].append(i)
#     for j in newdict:
#         if len(newdict[j]) == 1:
#             newdict[j] = newdict[j][0]
#     return newdict
# print(func({'a':1, 'b':2, 'c':2, 'd':1, 'e':5}))

# -------------------------------------------------

# '''8. Fibonacci'''

# def fibonacci(x):
#     if x == 1:
#         return 0
#     elif x == 2:
#         return 1
#     else:
#         return fibonacci(x-1) + fibonacci(x-2)

# print(fibonacci(5))