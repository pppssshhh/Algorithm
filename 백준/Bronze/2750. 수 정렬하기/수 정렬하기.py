n = int(input())
total = []

for _ in range(n):
  num = int(input())
  total.append(num)

total.sort()

for i in total:
  print(i)