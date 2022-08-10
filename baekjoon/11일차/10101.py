# 삼각형 외우기
import sys
sys.stdin = open('10101.txt')
a = int(input())
b = int(input())
c = int(input())
sum_ = a + b + c
if sum_ == 180 and a == b and a == c :
    print('Equilateral')
elif sum_ != 180 :
    print('Error')
elif sum_ == 180 and a != b and a != c and b != c: 
    print('Scalene')
else:
    print('Isosceles')