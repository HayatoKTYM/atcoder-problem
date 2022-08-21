"""
https://atcoder.jp/contests/atc001/tasks/unionfind_a
"""
n, q = map(int, input().split())
union_find = [i for i in range(n)]
# union_find = [0,1,2,3,4,5,1]

def get_root(num):
    # 根本
    if union_find[num] == num:
        return num
    # 根本でない場合，1つ上の根へ移動
    else:
        root = get_root(union_find[num])
        union_find[num] = root
        return root

def update_root(src, tgt):
    union_find[get_root(src)] = get_root(tgt)

def check_same_root(a, b):
    return get_root(a) == get_root(b)

for i in range(q):
    p, a, b = map(int, input().split())
    if p == 0:
        update_root(b, a)
    else:
        if check_same_root(a, b):
            print('Yes')
        else:
            print('No')

# print(union_find)