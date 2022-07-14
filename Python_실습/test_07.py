#주어진 리스트 numbers에서 최소값을 구하여 출력하시오.
#max() 함수 사용 금지
#numbers = [0, 20, 100, 50, -60, 50, 100] # -60
#numbers = [0, 1, 0] # 0
#numbers = [-10, -100, -30] # -30

numbers = [-10, -100, -30]

min = 0

for i in numbers:
    if i < min:
        min = i

print(min)