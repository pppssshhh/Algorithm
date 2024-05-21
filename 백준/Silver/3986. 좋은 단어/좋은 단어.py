n = int(input())
cnt = 0
for _ in range(n):
  alpha = list(input())
  stk = []
  for i in range(len(alpha)):
    if stk and (alpha[i] == stk[-1]):
      stk.pop()
    else:
      stk.append(alpha[i])

  if len(stk) == 0:
    cnt += 1

print(cnt)