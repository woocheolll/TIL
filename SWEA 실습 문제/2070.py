# 2개의 수를 입력 받아 크기를 비교하여 등호 또는 부등호를 출력하는 프로그램을 작성하라.

T = int(input())
for i in range(T):
    a, b = map(int,input().split())
    if a < b :
        print('<')
    elif a > b :
        print('>')
    else:
        print('=')
