# 1부터 n까지의 곱을 구하여 출력하는 코드를 1) while 문 2) for 문으로 각각 작성하시오.
# 1) while 문
n = 1 
a = 1
while n < 6:
    a = a * n
    print(n , a)
    n += 1



# 2) for 문

n = 0
a = 1
for i in range(0, 5):
    n += 1
    a = a * n
    print(n , a)

