# 듣보잡

# input
# 3 4
# ohhenrie
# charlie
# baesangwook
# obama
# baesangwook
# ohhenrie
# clinton
import sys
sys.stdin = open('input.txt')
# a, b = map(int,input().split())
# name = [input() for _ in range(a + b)]
# count_ = 0
# li = []
# for i in range(a):
    
#     for j in range(a, a+b):
#         if name[i] == name[j]:
#             count_+=1
#             li.append(name[i])           
# li.sort()          
# print(count_)
# print(*li,sep='\n')
N , M = map(int,input().split())
arr_1 = set()
arr_2 = set()

for _ in range(N):
    arr_1.add(input())
for _ in range(M):
    arr_2.add(input())

arr = sorted(list(arr_1 & arr_2))
print(len(arr))

for i in arr:
    print(i)