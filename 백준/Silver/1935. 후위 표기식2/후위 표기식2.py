n = int(input())

sentence = list(input()) # 후위 표기식

num = []            # num=[int(input()) for i in range(n)] 한 줄 코드로 가능
for _ in range(n):  # 숫자 피연산자 입력받기
  i = int(input())
  num.append(i)
  

stk = [] 
for x in sentence:
  if x.isalpha():    # 후위 표기식의 원소가 알파벳이면 알파벳에 맞는 숫자를 스택에 저장
    stk.append(num[ord(x) - 65])
  else:
    a = stk.pop()
    result = stk.pop()
    
    if x == "+":
      result += a

    elif x == '-':
      result -= a

    elif x == '*':
      result *= a

    elif x == '/':
      result /= a

    stk.append(result)

print('%.2f'%stk[-1])
    