"""
https://atcoder.jp/contests/typical90/tasks/typical90_p
"""

N = int(input())
coins = sorted(list(map(int, input().split())))
a, b, c = coins
ans = 10 ** 5
max_C = N // c

for i in range(min(9999, max_C), -1, -1):
    # print(f"{c}:{i}枚", end=" ")
    # Cでi枚使用した
    tmp = N - c * i
    # Bで使える最大枚数
    max_B = (N - (c * i)) // b
    for j in range(min(9999-i, max_B), -1, -1):
        # print(f"{b}:{j}枚", end=" ")
        if (tmp - b * j) % a == 0:
            count = i + j + (tmp - b*j) // a
            # print(i,j)
            if ans > count:
                ans = count
print(ans)