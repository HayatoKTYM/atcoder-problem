"""
https://atcoder.jp/contests/typical90/tasks/typical90_c
"""
from collections import deque


N = int(input())

map_lst = [[] for _ in range(N)]
for i in range(N-1):
    x, y = map(int, input().split())
    map_lst[x-1].append(y-1)
    map_lst[y-1].append(x-1)

register = [False] * N  # 既に来た都市をTrueに
pos_deque = deque([(0, 0)])  # 最初に都市1からSTART
max_dist_city = [0, 0]  # (都市名,距離)

# 都市1からの最短経路を算出 (最長都市を保存:max_dist_city)
while pos_deque:
    city, dist = pos_deque.popleft()
    # 最長距離都市の更新
    if max_dist_city[1] < dist:
        max_dist_city = [city, dist]

    # 訪問済み都市
    register[city] = True
    for next_city in map_lst[city]:
        # 経路がある AND まだ未訪問ならば追加
        if not register[next_city]:
            pos_deque.append((next_city, dist+1))  # 距離は+1する
    # print(pos_deque)

# print(max_dist_city) #都市1からの最長経路である都市と
pos_deque = deque([(max_dist_city[0], 0)])
register = [False] * N
max_dist_city = [max_dist_city[0], 0]
# 都市max_dist_city[0]からの最短経路を算出 (最長都市を保存:max_dist_city)
while pos_deque:
    city, dist = pos_deque.popleft()
    if max_dist_city[1] < dist:
        max_dist_city = [city, dist]

    register[city] = True
    for next_city in map_lst[city]:
        if not register[next_city]:
            pos_deque.append((next_city, dist+1))
    # print(pos_deque)
print(max_dist_city[1]+1)
