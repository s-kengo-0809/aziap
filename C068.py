'''
秘密の手紙
ある文字列(S)に対し、奇数番目の単語は逆方向、偶数番目は順方向に文字列(N)だけずらす
(ex)QEPG → MILK

結果：100点
'''

def crypt():
    N = int(input())
    S = input()
    t = ''
    for i in range(len(S)):
        if i % 2 == 0:
            t += chr(ord('Z') - (ord('Z') - ord(S[i]) + N) % 26)
        elif i % 2 == 1:
            t += chr(ord('A') + (ord(S[i]) - ord('A') + N) % 26)
    print(t)

if __name__ == '__main__':
    crypt()
