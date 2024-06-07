n, k = map(int,input().split())
score = list(map(int,input().split()))
score.sort()
cut = len(score) - k

print(score[cut])