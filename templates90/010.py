"""
https://atcoder.jp/contests/typical90/tasks/typical90_j
"""

N = int(input())

A = [0] * (N+1)
B = [0] * (N+1)
for i in range(1, N+1):
    c, p = map(int, input().split())
    if c == 1:
        A[i] = A[i-1] + p
        B[i] = B[i-1]
    else:
        A[i] = A[i-1]
        B[i] = B[i-1] + p

for _ in range(int(input())):
    l, r = map(int, input().split())
    # print(sum(A[l-1:r]), sum(B[l-1:r]))
    print(A[r] - A[l-1], B[r] - B[l-1])
