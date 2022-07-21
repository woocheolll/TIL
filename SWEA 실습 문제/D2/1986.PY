# 1부터 N까지의 숫자에서 홀수는 더하고 짝수는 뺐을 때 최종 누적된 값을 구해보자.
T = int(input())

for i in range(1, T + 1):
    N = int(input())
    sum = 1
    for j in range(2, N + 1):
        if j % 2 == 0:
            sum -= j
        else :
            sum += j
    
    print('#%d %d' % (i,sum))