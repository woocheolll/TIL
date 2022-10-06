# 회사에 있는 불쌍한 사람

import sys
sys.stdin = open('input.txt')
t = int(input())
name=[]
for _ in range(t): 
    a,b = input().split()
    if b == 'enter' :
        name.append(a)
    else:
        name.remove(a)
        
name.sort(reverse=True)

for i in name:
    print(i)
