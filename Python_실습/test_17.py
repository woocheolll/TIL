word = 'banana'

result = ''
for i in word:
    temp = ord(i)
    temp -= 32
    result += chr(temp)

print(result)