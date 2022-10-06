word = input()
count = -1
index = -1
for i in word:
    count +=1
    if i == 'a':
        index = count
        break
print(index)



word = input()
count = -1
index = -1
for i in word:
    count +=1
    if i == 'a':
        index = count
        print(index,end=' ')
