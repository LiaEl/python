classes = {}

def search(parent, child):
 if parent == child:
  return True
 if classes[child]['parents'] == []:
  return False
 if parent in classes[child]['parents']:
  return True
 for next_chld in classes[child]['parents']:
  if search(parent, next_chld):
   return True
 return False

n = int(input())
for _ in range(n):
 ar = [i for i in input().split() if i != ':']
 child = ar[0]
 classes[child] = {'parents' : ar[1:]}

q = int(input())
for _ in range(q):
 parent, child = input().split()
 if search(parent, child):
  print('Yes')
 else:
  print('No')