"""
002 - Encyclopedia of Parentheses（★3） 
実行時間制限: 2 sec / メモリ制限: 1024 MB

配点: 3 点

問題文
長さ N の正しいカッコ列をすべて、辞書順に出力してください。

ただし、正しいカッコ列は次のように定義されています :

() は正しいカッコ列である
S が正しいカッコ列であるとき、文字列 ( +S+ ) は正しいカッコ列である
S,T が正しいカッコ列であるとき、文字列 S+T は正しいカッコ列である
それ以外の文字列はすべて、正しいカッコ列でない
例えば、

()()
(()())(())
()()()()()()()()
は正しいカッコ列ですが、

)(
)))()(((
((((a))))
は正しいカッコ列ではありません。

また、 ( の方が ) よりも辞書順で早いものとします。

制約
1≤N≤20
N は整数

入力
入力は以下の形式で標準入力から与えられます。
N

出力
長さ N の正しいカッコ列をすべて、辞書順に、改行区切りで出力してください。
"""

N = int(input())

if N % 2 == 1:
    exit()
pattern = [('A', 1, 0)]
ans = []
while pattern:
    x, Acnt, Bcnt = pattern.pop(0)
    if len(x) >= N:
        if Acnt == Bcnt:
            ans.append(x)
        continue
    if Acnt == Bcnt:
        pattern.append((x+'A', Acnt+1, Bcnt))
    elif Acnt * 2 == N:
        pattern.append((x+'B', Acnt, Bcnt+1))
    elif Bcnt * 2 == N:
        pattern.append((x+'A', Acnt+1, Bcnt))
    else:
        pattern.append((x+'A', Acnt+1, Bcnt))
        pattern.append((x+'B', Acnt, Bcnt+1))


    #print(pattern)
for aa in sorted(ans):
    print(aa.replace('A','(').replace('B', ')'))