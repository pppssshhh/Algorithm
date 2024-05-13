n = int(input())
r=1
for _ in range(n):
  r *= n
  n -= 1
print(r)