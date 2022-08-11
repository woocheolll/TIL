#영수증
import sys
sys.stdin = open('25304.txt')
max_ = int(input())
n = int(input())
for i in range(n):
    money, m = map(int,input().split())
    max_ -= (money*m)
if max_ == 0:
    print('Yes')
else:
    print('No')

           