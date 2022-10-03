# 시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.
a = int(input())

if 100 >= a >= 90:
    print('A')
elif 90 > a >= 80:
    print('B')
elif 80 > a >= 70:
    print('C')
elif 70 > a >= 60:
    print('D')
else:
    print('F')