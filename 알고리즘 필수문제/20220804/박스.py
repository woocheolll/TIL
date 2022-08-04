#9455
import sys

sys.stdin = open('박스.txt')
a = int(input())
for _ in range(a):
    N,M = int(input().split())
    matrix = [list(input()) for _ in range(N)]
    for i in range(N):
        for j in range(M):
            print(matrix)