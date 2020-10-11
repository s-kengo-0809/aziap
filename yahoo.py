

time = list(map(int, input().split()))
time.append(time[0])
# print(time)
abs = [abs(time[i+1]-time[i]) for i in range(7)]
print(max(abs))
