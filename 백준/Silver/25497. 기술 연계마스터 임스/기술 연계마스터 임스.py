n = int(input())

skill = list(input())

stk = []
cnt = 0

for i in skill:
  if i == 'L' or i == 'S':
    stk.append(i)
  elif i == 'R':
    if 'L' in stk:
      stk.remove('L')
      cnt += 1
    else:
      break
  elif i == 'K':
    if 'S' in stk:
      stk.remove('S')
      cnt += 1
    else:
      break
  else:
    cnt += 1

print(cnt)