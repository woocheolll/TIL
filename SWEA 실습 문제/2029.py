# 몫과 나머지 출력하기 

T = int(input())
for i in range(T):
    a, b = map(int,input().split())
    print(i+1, a//b, a%b)