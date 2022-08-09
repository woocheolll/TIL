# 카드놀이


A = 0
B = 0
D = 'D'
carda = list(map(int,input().split()))
cardb = list(map(int,input().split()))
for i in range(10):
    if carda[i] > cardb[i] :
        A += 3
        D = 'A'
    elif carda[i] < cardb[i] :
        B += 3
        D = 'B'
    else:
        A += 1
        B += 1
        
if A > B :
    print(A, B)
    print('A')
elif A < B :
    print(A, B)
    print('B')

if A == B:
    if D =='A':
        print(A, B)
        print('A')
        
        
    if D =='B':
        print(A, B)
        print('B')
        
    if D =='D':
        print(A, B)
        print('D')


        
