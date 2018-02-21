class Trie:
  def __init__(self):
    self.dict = {}
    
  def add(self, word):
    current = self.dict
    for ch in word:
      if ch not in current:
        current[ch] = { "count": 0}
      current[ch]["count"] += 1;        
      current = current[ch]
        
  def begin_with(self,word):
    current = self.dict
    for ch in word:
      if ch not in current.keys():
        return 0
      current = current[ch]
    return current["count"]


n = int(input().strip())

contacts = Trie()

for a0 in range(n):
    op, contact = input().strip().split(' ')   
    if op == "add":
        contacts.add(contact)
    if op == "find":
        print(contacts.begin_with(contact))
