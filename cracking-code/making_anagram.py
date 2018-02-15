# Alice is taking a cryptography class and finding anagrams to be very useful. We consider two strings to be anagrams of each other if the first string's letters can be rearranged to form the second string. In other words, both strings must contain the same exact letters in the same exact frequency For example, bacdc and dcbac are anagrams, but bacdc and dcbad are not.

# Alice decides on an encryption scheme involving two large strings where encryption is dependent on the minimum number of character deletions required to make the two strings anagrams. Can you help her find this number?

# Given two strings,  and , that may or may not be of the same length, determine the minimum number of character deletions required to make  and  anagrams. Any characters can be deleted from either of the strings.

# This challenge is also available in the following translations:


from functools import reduce

def number_needed(a, b):
    count = [0]*26
    for c in a:
      count[ord(c) - 95] += 1
    for c in b:
      count[ord(c) - 95] -= 1

    return reduce((lambda x,y: abs(x) + abs(y)), count)

a = input().strip()
b = input().strip()

print(number_needed(a, b))