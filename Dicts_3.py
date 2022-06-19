# '''143. Анаграммы'''

# word1 = input('Enter first word: ').lower()
# word2 = input('Enter second word: ').lower()
# mylist1 = []
# mylist2 = []

# for i in word1:
#     mylist1.append(i)

# for j in word2:
#     mylist2.append(j)

# mylist1.sort()
# mylist2.sort()

# if mylist1 == mylist2:
#     print('Your entered words are anagrams')
# else:
#     print('Your entered words are not anagrams')

# ------------------------------------------------

# '''144. Снова анаграммы'''

# text1 = input('Enter first text: ').lower()
# text2 = input('Enter second text: ').lower()
# mylist1 = []
# mylist2 = []
# symbs = ".,;:!?' "

# for i in text1:
#     if i not in symbs:
#         mylist1.append(i)

# for j in text2:
#     if j not in symbs:
#         mylist2.append(j)

# mylist1.sort()
# mylist2.sort()

# if mylist1 == mylist2:
#     print('Your entered texts are anagrams')
# else:
#     print('Your entered texts are not anagrams')