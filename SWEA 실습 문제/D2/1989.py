T = int(input())

for i in range(1, T + 1):
    name = input()
    name2 = name[::-1]
    if name == name2 :
        name = 1
    else :
        name = 0
    
    
    
    
    
    
    
    
    
    
    
    
    print("#{} {}".format(i, name))