word = 'banana'
bcount = 0
acount = 0
ncount = 0
for i in word:

    if i == 'b' :
        bcount += 1
    elif i == 'a':
        acount += 1
    elif i == 'n':
        ncount += 1
        
print('b',bcount)
print('a',acount)
print('n',ncount)