# 2단부터 9단까지 반복하여 구구단을 출력하세요.
for i in range(2, 10):
    print('---',i,'단---')
    for j in range(1, 10):
        print(i,'X', j,'=' ,i*j)