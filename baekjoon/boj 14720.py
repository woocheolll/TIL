# 7
# 0 1 2 0 1 2 0
import sys
sys.stdin = open('input.txt')
n = int(input())
milk = list(map(int,input().split()))

count = 0

for i in range(n):
    if milk[i] == count % 3:
        count += 1

print(count)