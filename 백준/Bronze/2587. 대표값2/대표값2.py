num = []
for _ in range(5):
  n = int(input())
  num.append(n)

num.sort()
avg = sum(num) // 5

print(avg)
print(num[2])