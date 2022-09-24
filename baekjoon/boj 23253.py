import sys
sys.stdin = open('input.txt')
N, M = map(int, input().split())
result = 'Yes'
for _ in range(2*M):
    books = list(map(int,input().rstrip().split()))
    if books != sorted(books,reverse=True):
        result = 'No'
        break

print(result)