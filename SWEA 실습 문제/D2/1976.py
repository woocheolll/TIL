# 시 분으로 이루어진 시각을 2개 입력 받아, 더한 값을 시 분으로 출력하는 프로그램을 작성하라.
# (시각은 12시간제로 표시한다. 즉, 시가 가질 수 있는 값은 1시부터 12시이다.)


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