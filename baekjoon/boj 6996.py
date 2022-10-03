# 애너그램
import sys
sys.stdin = open('6996.txt')
t = int(input())
for test in range(t):
    a,b = input().split()
    a1 = sorted(list(a))
    b1 = sorted(list(b))
    

    if a1 == b1:
        print(f'{a} & {b} are anagrams.')
    else: 
        print(f'{a} & {b} are NOT anagrams.')