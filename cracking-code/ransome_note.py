def ransom_note(magazine, note):
    dict = {}
    for word in magazine:
        if word in dict.keys():
            dict[word] += 1
        else:
            dict[word] = 1
    
    for word in note:
      if word not in dict.keys():
        return False
      if word in dict.keys() and dict[word] > 0:
        dict[word] -= 1
      else:
        return False
    return True

m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print("Yes")
else:
    print("No")