"""
https://atcoder.jp/contests/typical90/tasks/typical90_a
2部探索で最大の長さを変えていく
K個に切れればもう少し大きくし，切れなければ小さくしていく
"""

N, L = map(int, input().split())

K = int(input())

A = list(map(int, input().split()))

ng = L
ok = 0

def is_ok(X):
  cur = 0
  cut = 0
  for i in range(len(A)):
    if A[i] - cur >= X: # 次のやつを加えてXを越えるならそこでカット
      cut += 1
      cur = A[i]
      if cut == K:
        rest = 0
        if L - cur >= X:
          return True
        return False
  return False
  
while abs(ok - ng) > 1:
  mid = abs(ok + ng) // 2
  print(f'{ok=},{ng=},{mid=}')
  if is_ok(mid):
    ok = mid
    print('ok')
  else:
    ng = mid
    print('ng')
    
print(ok)
