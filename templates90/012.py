"""
https://atcoder.jp/contests/typical90/tasks/typical90_l
"""
H, W = map(int, input().split())

map_lst = [[0] * W for _ in range(H)]

for _ in range(int(input())):
    t = input()
    if t[0] == '1':
        _, x, y = map(int, t.split())
        map_lst[x-1][y-1] = 1
    else:
        _, ra, ca, rb, cb = map(int, t.split())

        flag = False
        # 下から横へ
        for x in range(min(ra-1, rb-1), max(ra, rb)):
            #print(map_lst[x][ca-1], x,ca-1)
            if map_lst[x][ca-1] != 1:
                flag = False
                break
        else:
            flag = True
        flag2 = False
        for x in range(min(ca-1,cb-1), max(ca,cb)):
            #print(map_lst[rb-1][x], rb-1, x)
            if map_lst[rb-1][x] != 1:
                flag2 = False
                break
        else:
            flag2 = True

        if flag and flag2:
            print('Yes')
            continue

        # 横から下へ
        flag = False
        for x in range(min(ra-1, rb-1), max(ra, rb)):
            #print(map_lst[x][cb-1], x, cb-1)
            if map_lst[x][cb-1] != 1:
                flag = False
                break
        else:
            flag = True
        flag2 = False
        for x in range(min(ca-1, cb-1), max(ca,cb)):
            #print(map_lst[ra-1][x], ra-1, x)
            if map_lst[ra-1][x] != 1:
                flag2 = False
                break
        else:
            flag2 = True

        if flag and flag2:
            print('Yes')
            continue

        print('No')

    #print(map_lst)