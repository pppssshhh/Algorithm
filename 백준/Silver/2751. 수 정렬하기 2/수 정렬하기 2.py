import sys
input = sys.stdin.readline

n = int(input())

unsorted_list = []

for _ in range(n):
  unsorted_list.append(int(input()))

unsorted_list.sort()

for i in unsorted_list:
  print(i)