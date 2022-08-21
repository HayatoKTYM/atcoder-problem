"""
https://atcoder.jp/contests/typical90/tasks/typical90_g
"""

N = int(input())

A = list(map(int, input().split()))
A = sorted(A)
# print(A)
Q = int(input())

import bisect

for _ in range(Q):
    b = int(input())
    index = bisect.bisect_left(A, b)
    # print(index, b)
    if index == len(A):
        print(abs(b-A[N-1]))
    elif index == 0:
        print(abs(b-A[0]))
    else:
        print(min(abs(b-A[index-1]), abs(b-A[index])))
