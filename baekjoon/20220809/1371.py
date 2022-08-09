import sys
sys.stdin = open("1371.txt")
a = list(input())
en = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for i in range(len(en)):
    a.count(en[i])
print(max(a))
    
    
    