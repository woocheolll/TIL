#세로읽기
import sys
sys.stdin = open('10798.txt')
a = []
for i in range(5):
    a.append(input())


for i in range(max(len(e) for e in a)) :
    for j in range(5):
        if i < len(a[j]):
            print(a[j][i],end='')