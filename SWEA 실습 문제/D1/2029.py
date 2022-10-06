# 몫과 나머지 출력하기 

T = int(input())
for i in range(1, T +1):
    a, b = map(int,input().split())
    print( "#%d %d %d" % (i, a//b, a%b) )