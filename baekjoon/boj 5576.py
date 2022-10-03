#콘테스트
import sys
sys.stdin = open('5576.txt')

w = [int(input()) for _ in range(10)]
k = [int(input()) for _ in range(10)]
w.sort()
k.sort()
wsum = (w[7]+w[8]+w[9])
ksum = (k[7]+k[8]+k[9])
print(wsum,ksum)