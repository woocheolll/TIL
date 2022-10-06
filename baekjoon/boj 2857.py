#FBI
import sys
sys.stdin = open('2857.txt')
data=[]
for i in range(1,6):
    FBI = input()
    if 'FBI' in FBI:
        data.append(i)
        
if data:
    print(*data,end='')        
else:
    print('HE GOT AWAY!')
        
    


