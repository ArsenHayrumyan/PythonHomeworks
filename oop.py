# '''1. cenTury'''

# class Year:
#     def __init__(self, year:int) -> int:
#         self.year = year
#     def toCentury(self):
#         if self.year % 100 == 0:
#             return self.year // 100
#         else:
#             return self.year // 100 + 1

# y = Year(int(input('Enter year: ')))
# print(y.toCentury())

# -----------------------------------------

# '''2. PALindrOme'''

# class Polindrome:
#     def __init__(self, s:str) -> bool:
#         self.s = s
#     def isPolindrome(self):
#         return len(self.s) <= 1 or self.s == self.s[::-1]

# word = Polindrome(input('Enter word to check: '))
# print(word.isPolindrome())

# -----------------------------------------

# '''3. LARGesT'''

# class Product:
#     def __init__(self, inputList:list, newList = []) -> int:
#         self.inputList = inputList
#         self.newList = newList
#     def prod_func(self):
#         for i in range(0, (len(self.inputList) - 1)):
#             res = self.inputList[i] * self.inputList[i + 1]
#             self.newList.append(res)
#         self.newList.sort()
#         return self.newList[-1]

# ob = Product([3, 6, -2, -5, 7, 3])
# print(ob.prod_func())
        
# -----------------------------------------

# '''4. find HiGHesT wORd'''

# class HighestWord:
#     def __init__(self, inputList, outputList = []) -> list:
#         self.inputList = inputList
#         self.outputList = outputList
#     def Longest(self):
#         self.inputList.sort(key=len)
#         for i in self.inputList:
#             if len(i) == len(self.inputList[-1]):
#                 self.outputList.append(i)
#         return self.outputList

# inputList = ["aba", "aa", "ad", "vcd", "aba"]
# txt = HighestWord(inputList)
# print(f'allLongestStrings{inputList} = {txt.Longest()}')

# -----------------------------------------

# '''5. Lucky'''

# class Lucky:
#     def __init__(self, n:int, sum1 = 0, sum2 = 0) -> bool:
#         self.n = n
#         self.sum1 = sum1
#         self.sum2 = sum2
#     def check(self):
#         s = str(self.n)
#         for i in s[:(len(s) // 2)]:
#             self.sum1 += int(i)
#         for i in s[(len(s) // 2):]:
#             self.sum2 += int(i)
#         return self.sum1 == self.sum2

# ticket1 = Lucky(1230)
# ticket2 = Lucky(239017)
# print(ticket1.check())
# print(ticket2.check())

# -----------------------------------------

# '''6. LisT sORT'''

# class MySort:
#     def __init__(self, input_list, output_list=[]):
#         self.input_list = input_list
#         self.output_list = output_list
#     def tree_sort(self):
#         for i in self.input_list:
#             if i != -1:
#                 self.output_list.append(i)
#         self.output_list.sort()
#         for i in range(len(self.input_list)):
#             if self.input_list[i] != -1:
#                 self.input_list[i] = self.output_list[0]
#                 self.output_list.remove(self.output_list[0])
#         return self.input_list
# p = MySort([-1, 150, 190, 170, -1, -1, 160, 180])
# print(p.tree_sort())

# -----------------------------------------

# '''7. WeiGHT'''

# class Weight:
#     def __init__(self, w_list:list, o_list = []) -> list:
#         self.w_list = w_list
#         self.o_list = o_list
#     def w_sum(self):
#         sum1 = 0
#         sum2 = 0
#         for i in range(0, len(self.w_list), 2):
#             sum1 += self.w_list[i]
#         self.o_list.append(sum1)
#         for j in range(1, len(self.w_list), 2):
#             sum2 += self.w_list[j]
#         self.o_list.append(sum2)
#         return self.o_list
# mylist = [50, 60, 60, 45, 70]
# p = Weight(mylist)
# print(f'alternating sums {mylist} = {p.w_sum()}')
        



