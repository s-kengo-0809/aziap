'''
タクシーの運賃どれが安くてどれが高いか

タクシーAは初乗りめっちゃ安いけど、ちょっと乗るとすぐ金額上がる。タクシーBは初乗り高いけど、初乗り距離が長い。
みたいな感じで、入力した走行距離だったらどのタクシーに乗ったら最安ですか、的な

＜入力例1＞
2 700
600 200 200 400
900 800 400 500

※
タクシー種類　走行距離
A：初乗り距離　初乗り運賃　加算距離　加算運賃
B：初乗り距離　初乗り運賃　加算距離　加算運賃

＜出力例1＞
600 800

＜結果＞
ミスなし、だけどたまに計算時間少しかかってた
'''

N, dis = input().split()
N, dis = int(N),int(dis)

b = []
for i in range(N):
    a = input().split()
    if dis < int(a[0]):
        b.append(int(a[1]))
    else:
        drive = int(a[0])
        rate = int(a[1])
        while dis >= drive:
            drive += int(a[2])
            rate += int(a[3])
        b.append(rate)
        
print(min(b),max(b))


'''
#上二つはリスト内でfor文回すか、初心者っぽく丁寧にやるかの違いだけど、出力は同じ
#下二つはsplit()するかしないかでどう変わるか

N, dis = input().split()
a = [input().split() for i in range(int(N))]
print(a)
print(a[0])
print(a[0][0])

a = []
for i in range(int(N)):
    a.append(input().split())
print(a)
print(a[0])
print(a[0][0])

a = []
for i in range(int(N)):
    a.append(input())
print(a)
print(a[0])
print(a[0][0])



[['600', '200', '200', '400'], ['900', '800', '400', '500']]
['600', '200', '200', '400']
600
[['600', '200', '200', '400'], ['900', '800', '400', '500']]
['600', '200', '200', '400']
600
['600 200 200 400', '900 800 400 500']
600 200 200 400
6
'''
