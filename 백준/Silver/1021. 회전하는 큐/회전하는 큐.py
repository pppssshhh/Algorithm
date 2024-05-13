from collections import deque

n, m = map(int,input().split())
que = deque(range(1,n+1))

choice = list(map(int,input().split()))
cnt = 0

for x in choice:
  while(True):
    if x == que[0]:
      que.popleft()
      break
    else:
      while (True):
        if que.index(x) <= (len(que) / 2):
          que.rotate(-1)
          cnt += 1
          break
        else:
          que.rotate(1)
          cnt += 1
          break
print(cnt)
    
