N = int(input())
S = input()

target = 'atcoder'
for i in range(N):
    if S[i] == 'a':
        S = S[i:]
        N = len(S)
        break
else:
    exit(print(0))

# 時間超過 (TLE)

# from collections import deque
# Queue = deque([(0, 0, "")]) # sにおける何番目の文字を次にみるか, targetの何番目を一致させる必要があるか

# ans = 0
# i = 0
# while Queue:
#     next_index, next_target, cur = Queue.popleft()
#     # print(next_index, next_target, cur)
#     if cur == target:
#         ans += 1
#         continue
#     if next_index == len(S):
#         continue
#     # ほしい文字と一致したならば
#     if S[next_index] == target[next_target]:
#         Queue.append((next_index+1, next_target+1, cur+target[next_target]))

#     # 何もせず，Sのindexを+1するパターン
#     Queue.append((next_index+1, next_target, cur))

#     # print(Queue)

# print(ans % (10**9 + 7))

dp = [[0]*8 for _ in range(N+1)]
# print(S)
dp[0][0] = 1
for i in range(N):
    for j in range(8):
        dp[i+1][j] += dp[i][j]
        if j < 7 and S[i] == target[j]:
            dp[i+1][j+1] += dp[i][j]

# print(dp[-5:])
print(dp[N][7] % (10**9+7))