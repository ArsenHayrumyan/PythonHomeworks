# | -.-.-.-.-.-  Test - 1 -.-.-.-.-.- |
# ---------------------------------------------------------------
'''1. Write a function to find the longest common prefix 
string amongst an array of strings.If there is no common 
prefix, return an empty string "".'''
# ---------------------------------------------------------------
'''Example - 1'''
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
'''Example - 2'''
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
'''Example - 3'''
# Input: strs = ["reflower","flow","flight"]
# Output: ""
# ---------------------------------------------------------------
# Your code :)

# def prefix(mylist:list) -> str:
#     mylist.sort(key=len)
#     count = 0
#     while True:
#         if count == len(mylist) - 1:
#             print(mylist[0])
#             break
#         elif mylist[0] in mylist[count + 1][:len(mylist[0])]:
#             count += 1
#         else:
#             mylist[0] = mylist[0][:-1]

# list = ["flower","flow","flight"]
# prefix(list)

# ---------------------------------------------------------------
'''2. Given an integer x, return true if x is palindrome integer.
An integer is a palindrome when it reads the same backward as forward.
For example, 121 is a palindrome while 123 is not.'''
# ---------------------------------------------------------------
'''Example - 1'''
# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
'''Example - 2'''
# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
'''Example - 2'''
# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
# ---------------------------------------------------------------
# Your code :)

# def pol(s):
#     if len(s) <= 1:
#         return True
#     else:
#         return s[0] == s[-1] and pol(s[1:-1])
# num = int(input('Enter number: '))

# s_num = str(num)
# print(pol(s_num))

# ---------------------------------------------------------------
'''3. Given a string s consisting of words and spaces, return the length of the last word in the string.
A word is a maximal substring consisting of non-space characters only.'''
# ---------------------------------------------------------------
'''Example - 1'''
# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.
'''Example - 2'''
# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.
'''Example - 3'''
# Input: s = "luffy is still joyboy"
# Output: 6
# Explanation: The last word is "joyboy" with length 6.
# ---------------------------------------------------------------
# Your code :)

# def last_lenght(s:str) -> int:
#     s1 = s[::-1]
#     list1 = s1.split(' ')
#     for i in list1:
#         if i == '':
#             list1.remove(i)
#     return len(list1[0])
    
# MyText = input('Enter your text: ')
# print(f'The lenght of the last word of your text is {last_lenght(MyText)}.')

# ---------------------------------------------------------------
'''4. Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.'''
# ---------------------------------------------------------------
'''Example - 1'''
# Input: s = "()"
# Output: true
# ---------------------------------------------------------------
'''Example - 2'''
# Input: s = "()[]{}"
# Output: true
# ---------------------------------------------------------------
'''Example - 3'''
# Input: s = "(]"
# Output: false
# ---------------------------------------------------------------
# Your code :)

# def br(s:str) -> bool:
#     for i in range(0, len(s), 2):
#         return s[i] == '(' and s[i + 1] == ')' or s[i] == '{' and s[i + 1] == '}' or s[i] == '[' and s[i + 1] == ']'

# brackets = input('Enter brackets: ')        
# print(br(brackets))

# ---------------------------------------------------------------
'''5. You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.'''
# ---------------------------------------------------------------
'''Example - 1'''
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# ---------------------------------------------------------------
'''Example - 2'''
# Input: list1 = [], list2 = []
# Output: []
# ---------------------------------------------------------------
'''Example - 3'''
# Input: list1 = [], list2 = [0]
# Output: [0]
# ---------------------------------------------------------------
# Your code :)

# def merge(l1:list, l2:list) -> list:
#     new_list = l1 + l2
#     new_list.sort()
#     return new_list

# list1 = [1, 2, 4]
# list2 = [1, 3, 4]
# print(merge(list1, list2))

# ---------------------------------------------------------------