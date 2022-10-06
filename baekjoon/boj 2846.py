#오르막길
n = int(input())
li = list(map(int, input().split()))
a = 0
list_ = []
for i in range(n-1):
    if li[i] < li[i+1]:
        a += li[i+1] - li[i]
    else:
        list_.append(a)
        a = 0
list_.append(a)
print(max(list_))