#소가 길을 건너간 이유 1
import sys
sys.stdin = open('14467.txt')
t = int(input())
arr = {}
count = 0
for test in range(t):
    a,b = map(int, input().split())
    if a not in arr:
        arr[a] = b
    else:
        if arr[a] != b:
            count +=1
            arr[a] = b
 
print(count)   