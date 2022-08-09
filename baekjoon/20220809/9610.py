# 사분면
# 2차원 좌표 상의 여러 점의 좌표 (x,y)가 주어졌을 때, 각 사분면과 축에 점이 몇 개 있는지 구하는 프로그램을 작성하시오.
import sys
sys.stdin = open("9610.txt")
t = int(input())
q1 = 0
q2 = 0
q3 = 0
q4 = 0
axis = 0
for test in range(1,t+1):
    x,y = map(int,input().split())
    if x == 0 or y == 0: # 둘중 하나라도 0 이면 axis +1
        axis += 1
    elif x > 0 and y > 0 : # 둘다 양수면 q1 +1
        q1 += 1
    elif x < 0 and y > 0 : # X가 음수고 Y가 양수면 q2 +1
        q2 += 1
    elif x < 0 and y < 0 : # X가 음수고 Y도 음수면 q3 +1
        q3 += 1
    else: # 나머지 +1
        q4 += 1
        
print(f'Q1: {q1}')
print(f'Q2: {q2}')
print(f'Q3: {q3}')
print(f'Q4: {q4}')
print(f'AXIS: {axis}')