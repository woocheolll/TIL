a, b = input().split()

max_ = int(a.replace('5','6')) + int(b.replace('5','6'))
min_ = int(a.replace('6','5')) + int(b.replace('6','5'))
        
print(min_,max_)