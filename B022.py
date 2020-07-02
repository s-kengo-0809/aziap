'''
選挙の演説
・演説を行うごとに、有権者が支持する立候補者が変わる
・最終的に最も支持者が多い立候補者を求める
https://paiza.jp/challenges/82/show

※10回のケースの内、9回目で失敗した、要改良
'''

para = input()
M,N,K = int(para.split(' ')[0]),int(para.split(' ')[1]),int(para.split(' ')[2])

kouhosha = [0]*M
kouhosha.append(N)
for i in range(K):
    speech = int(input())
    if kouhosha[-1] != 0:
        kouhosha[-1] -= 1
        kouhosha[speech-1] += 1
    for j in range(0,M):
        if j == speech-1:
            continue
        elif kouhosha[j] != 0:
            kouhosha[j] -= 1
            kouhosha[speech-1] += 1
    
kouhosha.pop(-1)

list_get_max = []
for i, v in enumerate(kouhosha):
    if v == max(kouhosha):
        list_get_max.append(i)
if len(list_get_max) != 1:
    for i in list_get_max:
        print(list_get_max[i]+1)
else:
    print(list_get_max[0]+1)



'''
print(kouhosha)
max_value = max(kouhosha)
print(max_value)
max_index = []
#print([i for i,v in enumerate(kouhosha) if v == max(kouhosha)])

for i in range(M):
    if i == kouhosha.index(max_value):
        max_index = kouhosha.index(max_value)
        print('ha',max_index)
print(max_index)
'''
