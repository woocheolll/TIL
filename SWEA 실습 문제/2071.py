# 10개의 수를 입력 받아, 평균값을 출력하는 프로그램을 작성하라.

T = int(input())
for i in range(T):
    a = map(int,input().split())
    b = sum(a)
    print(i+1, round(b / 10))
