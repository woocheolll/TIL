
T = int(input())

for i in range(1, T + 1):
    N = int(input())
    list = [0]*10
    
    count = 0
    while(True) :
        if 0 not in list :
            break
        else : 
            count += 1
            a = str(N*count)
            for j in range(len(a)):
                list[int(a[j])] = 1
    print("#{} {}".format(i, a))
        