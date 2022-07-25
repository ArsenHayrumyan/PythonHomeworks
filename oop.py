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
