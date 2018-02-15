def is_matched(expression):
    open  = ["{", "[", "("]
    close = ["}", "]", ")"]
    stack = []
    for ch in expression:
      if ch in open:
        stack.append(ch)
      if ch in close:
        if len(stack) > 0 :
          tmp = stack.pop()
          idx = close.index(ch)
          if tmp != open[idx]:
            return False
        else:
          return False
    if len(stack) > 0:
      return False
    return True
    
                

t = int(input().strip())
for a0 in range(t):
    expression = input().strip()
    if is_matched(expression) == True:
        print("YES")
    else:
        print("NO")
