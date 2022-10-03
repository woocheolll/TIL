# 숫자카드
import sys
sys.stdin = open('input.txt')

_ = int(input())
n2= input().split()
_ = int(input())
m2= input().split()
for i in range(len(m2)):
    count_ = 0
    for j in range(len(n2)):
        if n2[j] == m2[i]:
            count_ += 1
    print(count_,end=' ')


# n = int(input())
# arr1 = list(map(int, input().split()))

# dict1 = dict()
# # 숫자카드와 개수를 딕셔너리에 담기
# for i in arr1:
#     if i in dict1:
#         dict1[i] += 1
#     else:
#         dict1[i] = 1


# m = int(input())
# arr2 = list(map(int, input().split()))

# for i in arr2:
#     if i in dict1:
#         print(dict1[i], end=' ')    # 존재하는 숫자 카드라면
#     else:
#         print(0, end=' ')           # 존재하지 않는 숫자 카드라면
