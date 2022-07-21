T = int(input())

for i in range(1, T + 1):
    a = 0
    b = 0
    time,minute,time2,minute2 = map(int,input().split())
    if time + time2 > 12 :
        a = time + time2 - 12
    else :
        a = time + time2 
        
    if minute + minute2 > 60 :
        b = minute + minute2 - 60
        a = a + 1
    else:
        b = minute + minute2
    
    print("#{} {} {}".format(i, a, b))