
import sys
sys.stdin = open('input.txt')
t = int(input())
dict = {}
for test in range(t):
    a = int(input())
    if a in dict :
        dict[a] += 1
    else:
        dict[a] = 1
    
dict = sorted(dict.items(), key=lambda x:(-x[1],x[0]))
print(dict[0][0])
    
    
        
