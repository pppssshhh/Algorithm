sentence = list(input())
stk = []

for x in sentence:
  if x.isdigit():
    stk.append(int(x))
  else:
    a = stk.pop()
    result = stk.pop()
    if x == '*':
      result = result * a
    elif x == '/':
      result = result // a
    elif x == '+':
      result = result + a
    elif x == '-':
      result = result - a
    
    stk.append(result)
      
print(stk[-1])