import sys
sys.stdin = open('2495.txt')

for _ in range(3):
    n = input()
    count = 0
    max = 1
    cur_n=n[0]
    for i in range(1,8):
        if n[i-1] == n[i]:
            count += 1
            if  count > max:
                max = count
            
        else:
             cur_n = n[i]
             count = 1
        
            
    print(max)