#주어진 숫자의 평균을 구하는 코드를 작성하시오.
#**sum(), len()  함수 사용 금지**
numbers = [3,10,20]
result = 0
a = 0
for i in numbers:
    result += i
    a += 1
avg = result / a
    
print(avg)