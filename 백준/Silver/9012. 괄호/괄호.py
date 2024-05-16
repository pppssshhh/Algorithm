t = int(input())

for _ in range(t):
  result = []
  ps = list(input())
  
  for i in range(len(ps)):
    if ps[i] == '(':
      result.append('(')
    else:
      try: result.pop()
      except:
        if len(result) == 0:
          result.append(')')
        break

  if len(result) == 0:
    print("YES")
  else:
    print("NO")
