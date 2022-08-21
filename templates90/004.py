"""
https://atcoder.jp/contests/typical90/tasks/typical90_d
"""

H, W = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(H)]

A_row = [0]*H
for i in range(H):
    A_row[i] = sum(A[i])

A_transpose = list(zip(*A))
A_col = [0]*W
for i in range(W):
    A_col[i] = sum(A_transpose[i])

# print(A_row)
# print(A_col)
ans = [[] for _ in range(H)]
for i in range(H):
    for j in range(W):
        ans[i].append(A_row[i]+A_col[j]-A[i][j])
    print(*ans[i])