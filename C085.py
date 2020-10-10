'''
あるアルファベットの文字列とそれぞれに対応した数字が割り当てられている。その文字列を左から順に出力していくのだが、
キーボードの耐久性の問題（そーゆう設定）で、出力したアルファベットに割り当てられていた数字が1減る。0になったら出力できない。
ディスプレイに最終的に出力されるアルファベット文字列を出力する

<入力例>
1 2 3 1 2 1 3 …　2 1　(26個分)
abcabcbcbcba

<結果>
ミスなし、99点
'''

taikyudo_list = list(map(int,input().split()))
alp = input()

disp = ''
for i in range(len(alp)):
    ascii = ord(alp[i]) - 97
    if taikyudo_list[ascii] >= 1:
        disp += alp[i]
        taikyudo_list[ascii] -= 1

print(disp)

