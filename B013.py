'''
再遅出社時刻
家⇔駅⇔駅⇔会社、それぞれ左から順にa,b,c分かかる。また、電車の本数Nが決まってて、それの線の時間が与えられる
この時、会社に8:59に着くのがベスト、これに近くなるよう最遅で家を出る時間を求める

結果：2ミス

入力例1
30 30 10
3
6 0
7 0
8 0

出力例1
07:30
'''


para = input()
a,b,c = int(para.split(' ')[0]),int(para.split(' ')[1]),int(para.split(' ')[2])
N = int(input())

h_mm = []
for i in range(N):
    h_mm.append(input())

train_go_time = []

if 59-c-b < 0:
    for i in range(N,0,-1):
        if int(h_mm[i-1].split(' ')[0]) == 8:     #h_mm[i-1][j] みたいにすれば、h_mm内の(i-1番目の要素)のさらに(j文字目)を取り出せるっぽい、splitなんて使わずに
            h_mm.pop(i-1)

for i in range(len(h_mm),0,-1):
    if int(h_mm[i-1].split(' ')[0]) == 8:
        if int(h_mm[i-1].split(' ')[-1]) > 59-c-b:
            continue
        else:
            train_go_time = h_mm[i-1]
            break
    else:
        train_go_time = h_mm[i-1]
        break

leave_home_mm = (int(train_go_time.split(' ')[-1])-a) % 60
leave_home_h = int(train_go_time.split(' ')[0])

if int(train_go_time.split(' ')[-1]) < a:
    print('0{}:{}'.format(leave_home_h - 1,leave_home_mm))
else:
    print('0{}:{}'.format(leave_home_h,leave_home_mm))
