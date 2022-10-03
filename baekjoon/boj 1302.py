# 베스트 셀러
import sys
sys.stdin = open('input.txt')
t = int(input())
b = {}

for test in range(t):
    a=input()
    if a not in b:
        b[a] =1
    else :
        b[a]+=1
    
li=[]
num = max(b.values())

for i in b:
    if num == b[i]:
        li.append(i)

li.sort()
print(li[0])

