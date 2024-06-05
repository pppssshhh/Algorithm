n = int(input())
line = list(map(int,input().split()))

stk = []

num = 1

for i in line:
  stk.append(i)
  while stk and stk[-1] == num:
    stk.pop()
    num += 1

if len(stk) == 0:
  print("Nice")
else:
  print("Sad")