# 정수 number가 주어질 때, 각 자릿수의 합을 구해서 출력하세요. 
number = int(input())
a = number // 100
b = number % 100 // 10
c = number % 100 % 10
print(a+b+c)
